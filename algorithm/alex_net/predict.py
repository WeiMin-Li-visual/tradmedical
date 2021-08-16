import os
import json
import torch
from PIL import Image
from torchvision import transforms
# import matplotlib.pyplot as plt

# from model import AlexNet
from algorithm.alex_net.model import AlexNet

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

def mainPredict(img_path, input_file_path, type_num):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose(
        [transforms.Resize((224, 224)),
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # load image
    # img_path = "test_red.bmp"
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
    # plt.imshow(img)#画图
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)

    # read class_indict
    # 文件输入目录
    input_path1 = os.path.join(input_file_path, "class_indices.json")  # 输入目录
    json_path = input_path1
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

    json_file = open(json_path, "r")
    class_indict = json.load(json_file)

    # create model
    # model = AlexNet(num_classes=5).to(device)
    model = AlexNet(num_classes=type_num).to(device)#改分类数

    # load model weights
    # 文件输入目录
    input_path2 = os.path.join(input_file_path, "AlexNet.pth")  # 输入目录
    weights_path = input_path2
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path, map_location=device))

    model.eval()
    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy()

    # print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
    #                                              predict[predict_cla].numpy())
    # print(print_res)
    # plt.title(print_res)
    # plt.show()
    return class_indict[str(predict_cla)], predict[predict_cla].numpy()

# if __name__ == '__main__':
#     main()
