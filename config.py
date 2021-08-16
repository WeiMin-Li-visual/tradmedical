#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 20:03
# @Author  : zhibindeng
# @Email   : zhibindeng@shu.deu.cn
# @File    : config.py

import os

IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())

UPLOADED_PHOTOS_DEST = os.path.dirname(os.path.realpath(__file__)) + '/uploadData/images'
UPLOADED_PHOTOS_SSL = os.path.dirname(os.path.realpath(__file__)) + '/files/ssl/'
UPLOADED_PHOTOS_ALLOW = IMAGES
