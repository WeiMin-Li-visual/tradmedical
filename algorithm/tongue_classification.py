import pandas as pd
from PIL import Image
import os
import numpy as np
from torchvision import transforms as T
import matplotlib.pyplot as plt
import torch
import os
import shutil
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# # 对舌的标签描述进行编码
# tongue['tongue_proper_color'] = 0  # 舌质颜色 淡红（正常）0 淡白1 红2 暗/紫3
# tongue['tongue_proper_shape_pang'] = 0  # 舌质形态 正常0 胖1  裂纹齿印(太少不用)
# tongue['tongue_proper_shape_neng'] = 0  # 舌质形态 正常0  嫩1
# tongue['tongue_proper_shape_chi'] = 0  # 舌质形态 正常0  有齿痕或齿印 1
# tongue['tongue_moss_color'] = 0  # 苔色白（正常）0 黄1
# tongue['tongue_moss_nature'] = 0  # 苔质 薄（正常）0  少1  腻2

#舌质颜色，标签归类
lable = pd.read_csv(r'../files/tongue_all_features_aug.csv')
proper_color_list=['light_red', 'pale_white', 'red', 'dark_purple']
proper_shape_pang_list=['normal', 'pang']
proper_shape_neng_list=['normal', 'neng']
proper_shape_chi_list=['normal', 'chi']
proper_moss_nature_list=['thin', 'few', 'greasy']
#遍历标签表
for index,row in lable.iterrows():
    id = row["id"]
    tongue = row["tongue"]
    color = row["tongue_proper_color"]
    shape_pang = row["tongue_proper_shape_pang"]
    shape_neng = row["tongue_proper_shape_neng"]
    shape_chi = row["tongue_proper_shape_chi"]
    moss_color = row["tongue_moss_color"]
    moss_nature = row["tongue_moss_nature"]
    # print(row.tolist())
    # print(index)

    #舌质颜色，标签归类
    # img_path=r'../files/tongueimage_aug/'
    # out_path=r'../files/tongue_image_data_set/tongue_proper_color/'+proper_color_list[color]+'/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)

    # 舌质形态（胖），标签归类
    # img_path = r'../files/tongueimage_aug/'
    # out_path = r'../files/tongue_image_data_set/tongue_shape_pang/' + proper_shape_pang_list[shape_pang] + '/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)

    # # 舌质形态（嫩），标签归类
    # img_path = r'../files/tongueimage_aug/'
    # out_path = r'../files/tongue_image_data_set/tongue_shape_neng/' + proper_shape_neng_list[shape_neng] + '/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)

    # # 舌质形态（齿痕或齿印），标签归类
    # img_path = r'../files/tongueimage_aug/'
    # out_path = r'../files/tongue_image_data_set/tongue_shape_chi/' + proper_shape_chi_list[shape_chi] + '/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)

    # # 苔质形态，标签归类
    # img_path = r'../files/tongueimage_aug/'
    # out_path = r'../files/tongue_image_data_set/tongue_moss_nature/' + proper_moss_nature_list[moss_nature] + '/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)

lable2 = pd.read_csv(r'../files/moss_all_features_aug.csv')
tongue_moss_color_list=['moss_white', 'moss_yellow']
#遍历标签表
for index,row in lable2.iterrows():
    id = row["id"]
    tongue = row["tongue"]
    color = row["tongue_proper_color"]
    shape_pang = row["tongue_proper_shape_pang"]
    shape_neng = row["tongue_proper_shape_neng"]
    shape_chi = row["tongue_proper_shape_chi"]
    moss_color = row["tongue_moss_color"]
    moss_nature = row["tongue_moss_nature"]
    # print(row.tolist())
    # print(index)

    #舌质颜色，标签归类
    # img_path=r'../files/moss_aug/'
    # out_path=r'../files/tongue_image_data_set/tongue_moss_color/'+tongue_moss_color_list[moss_color]+'/'
    # oldname = img_path + id + '.bmp'
    # outname = out_path + id + '.bmp'
    # shutil.copyfile(oldname, outname)