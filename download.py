import os
# 设置环境变量以使用国内镜像源
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com/'
from transformers import AutoModelForImageSegmentation


# 定义模型名称和本地保存路径
model_names = ["ZhengPeng7/BiRefNet", "ZhengPeng7/BiRefNet_lite"]
local_path = "./data"

# 下载并保存模型到本地
for model_name in model_names:
    model = AutoModelForImageSegmentation.from_pretrained(model_name, trust_remote_code=True, cache_dir=local_path)
    print(f"Model {model_name} saved to {local_path}")

print("Models loaded successfully.")