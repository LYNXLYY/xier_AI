import pandas as pd
import matplotlib.pyplot as plt

a1 = pd.read_csv("D:\\ApythonProject\\pytorch01\\Begin01\\xi_er\\example.csv")
print(a1)
x1 = a1.iloc[1:, 0]
y1 = a1.iloc[1:, 2]
x2 = a1.iloc[1:, 1]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 13

label_counts = {}

# 遍历数据，统计每个标签的数量
for label in x2:
    if label in label_counts:
        label_counts[label] += 1
    else:
        label_counts[label] = 1

x_labels = list(label_counts.keys())  # 提取键作为横坐标

y_values = list(label_counts.values())  # 提取值作为纵坐标

# 创建条形图
plt.bar(x_labels, y_values)

# 添加标题和标签
plt.title("日期和通知数的关系")
plt.xlabel("日期")
plt.ylabel("通知数")

# 显示条形图
plt.show()

plt.title("通知人和下载次数的关系")
plt.xlabel("通知人")
plt.ylabel("下载次数")
plt.bar(
    x1, y1, width=0.5, bottom=0, align="edge", color="b", edgecolor="w", linewidth=2
)
plt.show()