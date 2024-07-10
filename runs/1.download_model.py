import clip
import torch

model, preprocess = clip.load('ViT-B/32')  # 例如，下载 ViT-B/32 模型