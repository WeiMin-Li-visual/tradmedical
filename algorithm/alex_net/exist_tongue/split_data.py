import os
from algorithm.alex_net import split_data

def main():
    # 指向你解压后的flower_photos文件夹
    cwd = os.getcwd()
    data_root = os.path.abspath(os.path.join(cwd, "../../../files"))  # get data root path，改目录
    input_img_path = os.path.join(data_root, "tongue_image_expansion", "exist_tongue")  # flower data set path,改目录
    # 建立保存验证集的文件夹
    output_img_path = os.path.join(data_root, "tongue_image_train_test_set", "exist_tongue")#改测试集划分目录
    split_data.mainSplitData(input_img_path, output_img_path)


if __name__ == '__main__':
    main()
