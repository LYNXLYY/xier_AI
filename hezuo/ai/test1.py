from flask import Flask, request, jsonify
import requests
from io import BytesIO
import torch
import numpy as np
from torchvision import models, transforms
from PIL import Image
from sklearn.neighbors import NearestNeighbors

# 初始化 Flask 应用
app = Flask(__name__)

# 配置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义图像预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 加载预训练的生成模型部分
model = models.resnet50(pretrained=True).to(device)
model.eval()  # 使用模型的中间层作为特征提取器


def extract_features(image):
    """ 提取图像特征 """
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model(image)  # 假设我们可以修改这里调用中间层
    return features.cpu().numpy().flatten()


def download_image(url):
    """ 从URL下载图像 """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert('RGB')
    return image


@app.route('/build_feature_database', methods=['POST'])
def build_feature_database():
    """ 构建特征数据库 """
    image_urls = request.json.get('image_urls')
    feature_list = []
    image_paths = []

    for url in image_urls:
        image = download_image(url)
        features = extract_features(image)
        feature_list.append(features)
        image_paths.append(url)

    feature_list_np = np.array(feature_list)
    return jsonify({
        'features': feature_list_np.tolist(),
        'image_paths': image_paths
    })


@app.route('/find_similar_images', methods=['POST'])
def find_similar_images():
    """ 查找最相似的图像 """
    query_image_url = request.json.get('query_image_url')
    feature_list = np.array(request.json.get('feature_list'))
    image_paths = request.json.get('image_paths')
    top_k = request.json.get('top_k', 5)

    query_image = download_image(query_image_url)
    query_features = extract_features(query_image)
    nbrs = NearestNeighbors(n_neighbors=top_k).fit(feature_list)
    distances, indices = nbrs.kneighbors([query_features])
    similar_images = [image_paths[i] for i in indices[0]]

    return jsonify({
        'similar_images': similar_images
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

