# 环境配置
[English Doc](./install_guide.md)

本文档陈述了搭建Real3D-Portrait Python环境的步骤，我们使用了Conda来管理依赖。

以下配置已在 A100/V100 + CUDA11.7 中进行了验证。


# 1. 安装CUDA
我们使用了CUDA extensions [torch-ngp](https://github.com/ashawkey/torch-ngp)，建议手动从[官方](https://developer.nvidia.com/cuda-toolkit)渠道安装CUDA。我们推荐安装CUDA `11.7`，其他CUDA版本（例如`10.2`）也可能有效。 请确保你的CUDA path(一般是 `/usr/local/cuda`) 指向了你需要的CUDA版本（例如 `/usr/local/cuda-11.7`）. 需要注意的是，我们目前不支持CUDA 12或者更高版本。

# 2. 安装Python依赖
```
cd <Real3DPortraitRoot>
source <CondaRoot>/bin/activate
conda create -n real3dportrait python=3.9
conda activate real3dportrait
conda install conda-forge::ffmpeg # ffmpeg with libx264 codec to turn images to video

# 我们推荐安装torch2.0.1+cuda11.7. 已经发现 torch=2.1+cuda12.1 会导致 torch-ngp 错误
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia

# 从源代码安装，需要比较长的时间 (如果遇到各种time-out问题，建议使用代理)
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"

# MMCV安装
pip install cython
pip install openmim==0.3.9
mim install mmcv==2.1.0 # 使用mim来加速mmcv安装

# 其他依赖项
pip install -r docs/prepare_env/requirements.txt -v

```
