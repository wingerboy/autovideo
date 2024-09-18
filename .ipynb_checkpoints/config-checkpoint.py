# -*- coding: utf-8 -*-
"""
配置文件
"""
from pydantic import BaseModel
import os


class Config(BaseModel):
    # 基础配置
    output_images_path = '' # 输出图片路径
    output_video_path = '' # 输出视频路径
    output_music_path = '' # 输出音乐路径

    # 文本内容生成

    # 图片内容生成

    # 音乐生成

    # 


conigs = Config()