# 原项目README
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

# 修改内容

- 移除app.py的测试视频
- 加入gradio的share

# python 3.10版

克隆项目
```shell
git clone https://ghp.ci/https://github.com/xy3xy3/video-background-removal
cd video-background-removal
```

换源（非必须）
```shell
conda config --remove-key channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
conda config --show channels
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

环境创建
```shell

conda create -n video-background-removal python=3.10.8 -y
conda activate video-background-removal
```

torch安装 conda版（和下面二选一）
```shell
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=11.8 -c pytorch -c nvidia -y
```

torch安装 pip版（和上面二选一）
```shell
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2
```


环境安装
```shell
pip install -r requirements.txt
```

frpc安装
```shell
wget https://wp.007irs.com/f/J35g6H4/frpc_linux_amd64
mv frpc_linux_amd64 frpc_linux_amd64_v0.3
chmod +x frpc_linux_amd64_v0.2
mv frpc_linux_amd64_v0.3 /root/miniconda3/envs/video-background-removal/lib/python3.10/site-packages/gradio
```

加速下载模型（如果不好访问hugging face，推荐先执行这个）
```shell
python download.py
```

运行
```shell
python app.py
```

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

环境安装
```shell
pip install -r requirements.txt
```

加速下载模型（如果不好访问hugging face，推荐先执行这个）
```shell
python download.py
```

运行
```shell
python app.py
```