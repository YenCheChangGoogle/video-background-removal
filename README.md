---
title: Video Background Removal
emoji: 📽️
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 5.1.0
app_file: app.py
pinned: true
short_description: Remove/Change background of video.
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# python 3.11版

克隆项目
```shell
git clone https://ghp.ci/https://github.com/xy3xy3/video-background-removal
cd video-background-removal
```

环境创建
```shell
conda create -n video-background-removal python=3.11 -y
conda activate video-background-removal
```
torch安装(cuda)
```shell
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y
```

# python 3.10版

克隆项目
```shell
git clone https://ghp.ci/https://github.com/xy3xy3/video-background-removal
cd video-background-removal
```

环境创建
```shell
conda create -n video-background-removal python=3.10 -y
conda activate video-background-removal
```
torch安装(cuda)
```shell
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
```

# 剩下的一样


环境安装
```python
pip install -r requirements.txt
```

加速下载模型（如果不好访问hugging face，推荐先执行这个）
```python
python download.py
```

运行
```python
python app.py
```