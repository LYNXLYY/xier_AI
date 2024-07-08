import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
from sklearn.neighbors import NearestNeighbors
import os
from tqdm import tqdm
# 初始化设备
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

def extract_features(image_path):
    """ 提取图像特征 """
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model(image)  # 假设我们可以修改这里调用中间层
    return features.cpu().numpy().flatten()

def build_feature_database(image_directory):
    """ 构建特征数据库 """
    feature_list = []
    image_paths = []
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_directory, filename)
            features = extract_features(image_path)
            feature_list.append(features)
            image_paths.append(image_path)
    return np.array(feature_list), image_paths

def find_similar_images(query_image_path, feature_list, image_paths, top_k=3):
    """ 查找最相似的图像 """
    query_features = extract_features(query_image_path)
    nbrs = NearestNeighbors(n_neighbors=top_k).fit(feature_list)
    distances, indices = nbrs.kneighbors([query_features])
    return [image_paths[i] for i in indices[0]]


data_dir = "E:\\Adataset\\Caltech101\\caltech101\\101_ObjectCategories\\airplanes"
query_image = "E:\\Adataset\\Caltech101\\caltech101\\101_ObjectCategories\\airplanes\\image_0003.jpg"
features, paths = build_feature_database(data_dir)



print(features.shape)
similar_images = find_similar_images(query_image, features, paths)


for image in similar_images:
    print(image)
