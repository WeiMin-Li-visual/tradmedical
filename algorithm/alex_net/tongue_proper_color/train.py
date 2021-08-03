import os
from algorithm.alex_net import train

def main():
    #输入目录
    data_root = os.path.abspath(os.path.join(os.getcwd(), "../../../files"))  # get data root path，改目录
    input_img_path = os.path.join(data_root, "tongue_image_train_test_set", "tongue_proper_color")  # flower data set path,改目录
    # 建立保存验证集的文件夹
    output_path = os.path.join(os.getcwd())  # 改输出目录
    type_num = 4
    epoch_num = 30
    train.mainTrain(input_img_path, output_path, type_num, epoch_num)


if __name__ == '__main__':
    main()
