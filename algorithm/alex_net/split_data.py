import os
from shutil import copy, rmtree
import random


def mk_file(file_path: str):
    if os.path.exists(file_path):
        # 如果文件夹存在，则先删除原文件夹在重新创建
        rmtree(file_path)
    os.makedirs(file_path)


def mainSplitData(input_img_path, output_img_path):
    # 保证随机可复现
    random.seed(0)

    # 将数据集中10%的数据划分到验证集中
    # split_rate = 0.1
    split_rate = 0.3

    # 指向你解压后的flower_photos文件夹
    # cwd = os.getcwd()
    # data_root = os.path.join(cwd, "../../../files/tongue_image_data_set")
    # origin_flower_path = os.path.join(data_root, "tongue_proper_color")
    # data_root = os.path.abspath(os.path.join(cwd, "../../../files"))  # get data root path，改目录
    # origin_flower_path = os.path.join(data_root, "tongue_image_data_set", "tongue_proper_color")  # flower data set path,改目录
    origin_flower_path = input_img_path
    assert os.path.exists(origin_flower_path), "path '{}' does not exist.".format(origin_flower_path)

    flower_class = [cla for cla in os.listdir(origin_flower_path)
                    if os.path.isdir(os.path.join(origin_flower_path, cla))]

    # 建立保存训练集的文件夹
    # train_root = os.path.join(data_root, "tongue_image_train_test_set", "tongue_proper_color", "train")#改训练集划分目录
    train_root = os.path.join(output_img_path, "train")  # 改训练集划分目录
    mk_file(train_root)
    for cla in flower_class:
        # 建立每个类别对应的文件夹
        mk_file(os.path.join(train_root, cla))

    # 建立保存验证集的文件夹
    # val_root = os.path.join(data_root, "tongue_image_train_test_set", "tongue_proper_color","val")#改测试集划分目录
    val_root = os.path.join(output_img_path, "val")  # 改测试集划分目录
    mk_file(val_root)
    for cla in flower_class:
        # 建立每个类别对应的文件夹
        mk_file(os.path.join(val_root, cla))

    # print(data_root)
    print(origin_flower_path)
    print(output_img_path)
    print(train_root)
    print(val_root)

    for cla in flower_class:
        cla_path = os.path.join(origin_flower_path, cla)
        images = os.listdir(cla_path)
        num = len(images)
        # 随机采样验证集的索引
        eval_index = random.sample(images, k=int(num*split_rate))
        for index, image in enumerate(images):
            if image in eval_index:
                # 将分配至验证集中的文件复制到相应目录
                image_path = os.path.join(cla_path, image)
                new_path = os.path.join(val_root, cla)
                copy(image_path, new_path)
            else:
                # 将分配至训练集中的文件复制到相应目录
                image_path = os.path.join(cla_path, image)
                new_path = os.path.join(train_root, cla)
                copy(image_path, new_path)
            print("\r[{}] processing [{}/{}]".format(cla, index+1, num), end="")  # processing bar
        print()

    print("processing done!")


# if __name__ == '__main__':
#     main()
