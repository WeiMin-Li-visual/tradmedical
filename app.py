from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)
import random
import time
import os
import config
from algorithm.alex_net import predict
from algorithm.yolov3 import yolo_tongue

#定义全局变量，避免每次调用
yolo = yolo_tongue.YOLO()

@app.route('/')
def hello_world():
    return 'Hello World!'

# 舌头检测
# returen 二元组：results = ('img/out/test1_crop_out.bmp', True)
def tongue_identify(input_path):
    out_path = './uploadData/images/crop'
    results = yolo.detect_image(input_path, out_path)
    # if results[1]:
    #     print('检测图片保存成功！')
    # else:
    #     print('没有检测到清晰舌头，请靠近重拍！')
    return results


# 舌诊
@app.route('/tongue/uploadimage', methods=['POST', "GET"])
def tongue_upload_image():
    fn = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(0, 100) + '.png'
    image = request.files.get('image')
    pic_dir = os.path.join(config.UPLOADED_PHOTOS_DEST, fn)
    image.save(pic_dir)

    results = tongue_identify(pic_dir)
    # 7yolo预测有无舌头，标签含义：【True,False】==【检测存在1、 检测不存在0】
    tongue_exist = {True: 1, False: 0}
    if not results[1]:
        print('没有检测到清晰舌头，请靠近重拍！')
        result_data = {'tongue_exist': 0}
        return json.dumps(result_data)

    #利用人类裁剪图 & 舌像图 进行二分类判断是否有舌头，效果不佳，只是输出看看，没有写入传给前端
    # 0预测【有无舌头】，标签含义：【exist、non_exist】==【存在、不存在】
    exist_tongue = {'exist': 1, 'non_exist': 0}
    img_path = results[0]  # 输入图片目录
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'exist_tongue')  # 输入模型文件目录
    type_num = 2
    type_result0, prob0 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率
    print('分类结果：' + str(type_result0) + '概率：' + str(prob0))
    if not str(type_result0)=='non_exist':
        print('没有检测到清晰舌头，请靠近重拍！')
        result_data = {'tongue_exist': 0}
        return json.dumps(result_data)

    # 1预测【舌质颜色】，标签含义：【dark_purple、light_red、pale_white、red】==【暗/紫3、淡红0、淡白1、红2】
    tongue_proper_color = {'dark_purple': 3, 'light_red': 0, 'pale_white': 1, 'red': 2}
    img_path = results[0]  # 输入图片目录
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_proper_color')  # 输入模型文件目录
    type_num = 4
    type_result1, prob1 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 2预测【舌质形态】，标签含义：【normal、pang】==【正常0、胖1】
    tongue_shape_pang = {'normal': 0, 'pang': 1}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_pang')  # 输入模型文件目录
    type_num = 2
    type_result2, prob2 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 3预测【舌质形态】，标签含义：【normal、neng】==【正常0、 嫩2】
    tongue_shape_neng = {'normal': 0, 'neng': 2}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_neng')  # 输入模型文件目录
    type_num = 2
    type_result3, prob3 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 4预测【舌质形态】，标签含义：【normal、chi】==【正常0、 有齿痕/齿印3】
    tongue_shape_chi = {'chi': 3, 'normal': 0 }
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_chi')  # 输入模型文件目录
    type_num = 2
    type_result4, prob4 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 5预测【苔色】，标签含义：【moss_white、moss_yellow】==【苔色白0、 苔色黄1】
    tongue_moss_color = {'moss_white': 0, 'moss_yellow': 1}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_moss_color')  # 输入模型文件目录
    type_num = 2
    type_result5, prob5 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 6预测【苔质】，标签含义：【few、greasy、thin】==【少2、 腻1、薄（正常）0】
    tongue_moss_nature = {'few': 2, 'greasy': 1, 'thin': 0}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_moss_nature')  # 输入模型文件目录
    type_num = 3
    type_result6, prob6 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    result_data = {'tongue_proper_color': tongue_proper_color[type_result1], 'tongue_proper_color_prob': str(prob1), \
                   'tongue_shape_pang': tongue_shape_pang[type_result2], 'tongue_shape_pang_prob': str(prob2), \
                   'tongue_shape_neng': tongue_shape_neng[type_result3], 'tongue_shape_neng_prob': str(prob3), \
                   'tongue_shape_chi': tongue_shape_chi[type_result4], 'tongue_shape_chi_prob': str(prob4), \
                   'tongue_moss_color': tongue_moss_color[type_result5], 'tongue_moss_color_prob': str(prob5), \
                   'tongue_moss_nature': tongue_moss_nature[type_result6], 'tongue_moss_nature_prob': str(prob6), \
                   'tongue_exist': tongue_exist[results[1]]}
    return json.dumps(result_data)


# 面诊
@app.route('/face/uploadimage', methods=['POST', "GET"])
def face_upload_image():
    # TODO
    return json.dumps("敬请期待")


# 掌诊
@app.route('/palm/uploadimage', methods=['POST', "GET"])
def palm_upload_image():
    # TODO
    return json.dumps("敬请期待")


if __name__ == '__main__':
    # pem_path = os.path.join(config.UPLOADED_PHOTOS_SSL, '6121517_lib61504.top.pem')
    # pem_key = os.path.join(config.UPLOADED_PHOTOS_SSL, '6121517_lib61504.top.key')
    # app.run(host='0.0.0.0', port=9200, debug=True, ssl_context=(pem_path, pem_key))
    app.run(host='0.0.0.0', port=9200, debug=True)
