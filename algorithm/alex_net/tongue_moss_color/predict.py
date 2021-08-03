import os
from algorithm.alex_net import predict

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

def main():
    # 输入图片目录
    img_path = "test_moss_yellow.bmp"
    img_path = os.path.join(os.getcwd(), img_path)  # 改输入文件目录
    # 输入数据文件夹
    input_file_path = os.path.join(os.getcwd())  # 改输入文件目录
    type_num = 2
    type_result, prob = predict.mainPredict(img_path, input_file_path, type_num)
    print(type(type_result))
    print(type_result)
    print(type(prob))
    print(prob)

if __name__ == '__main__':
    main()
