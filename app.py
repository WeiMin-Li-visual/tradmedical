from flask import Flask,render_template,request,jsonify,json
# from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class

app = Flask(__name__)
import random
import time
import os
import cinfig
from algorithm.alex_net import predict

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['POST',"GET"])
def login():
    print(request.data)
    return jsonify({'status':True})

@app.route('/uploadImage',methods=['POST',"GET"])
def uploadImage():
    fn = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(0, 100) + '.png'
    image = request.files.get('image')
    pic_dir = os.path.join(cinfig.UPLOADED_PHOTOS_DEST, fn)
    print(pic_dir)
    image.save(pic_dir)

    # 1预测【舌质颜色】，标签含义：【dark_purple、light_red、pale_white、red】==【暗/紫、淡红、淡白、红】
    tongue_proper_color = {'dark_purple': '暗/紫', 'light_red': '淡红', 'pale_white': '淡白', 'red': 'red'}
    img_path = pic_dir  # 输入图片目录
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_proper_color')  # 输入模型文件目录
    type_num = 4
    type_result1, prob1 = predict.mainPredict(img_path, input_file_path, type_num)#列表里的key，概率

    # 2预测【舌质形态】，标签含义：【normal、pang】==【正常、胖】
    tongue_shape_pang = {'normal': '正常', 'pang': '胖'}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_pang')  # 输入模型文件目录
    type_num = 2
    type_result2, prob2 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 3预测【舌质形态】，标签含义：【normal、neng】==【正常、 嫩】
    tongue_shape_neng = {'normal': '正常', 'neng': '嫩'}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_neng')  # 输入模型文件目录
    type_num = 2
    type_result3, prob3 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 4预测【舌质形态】，标签含义：【normal、chi】==【正常、 有齿痕/齿印】
    tongue_shape_chi = {'chi': '有齿痕/齿印', 'normal': '正常'}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_shape_chi')  # 输入模型文件目录
    type_num = 2
    type_result4, prob4 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 5预测【苔色】，标签含义：【moss_white、moss_yellow】==【苔色白、 苔色黄】
    tongue_moss_color = {'moss_white': '苔色白', 'moss_yellow': '苔色黄'}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_moss_color')  # 输入模型文件目录
    type_num = 2
    type_result5, prob5 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    # 6预测【苔质】，标签含义：【few、greasy、thin】==【少、 腻、薄（正常）】
    tongue_moss_nature = {'few': '少', 'greasy': '腻', 'thin': '薄'}
    # 模型文件夹
    input_file_path = os.path.join(os.getcwd(), 'algorithm', 'alex_net', 'tongue_moss_nature')  # 输入模型文件目录
    type_num = 3
    type_result6, prob6 = predict.mainPredict(img_path, input_file_path, type_num)  # 列表里的key，概率

    result_data = {'tongue_proper_color':tongue_proper_color[type_result1], 'tongue_proper_color_prob':str(prob1),\
                   'tongue_shape_pang':tongue_shape_pang[type_result2], 'tongue_shape_pang_prob':str(prob2), \
                   'tongue_shape_neng': tongue_shape_neng[type_result3], 'tongue_shape_neng_prob': str(prob3), \
                   'tongue_shape_chi': tongue_shape_chi[type_result4], 'tongue_shape_chi_prob': str(prob4), \
                   'tongue_moss_color': tongue_moss_color[type_result5], 'tongue_moss_color_prob': str(prob5), \
                   'tongue_moss_nature': tongue_moss_nature[type_result6], 'tongue_moss_nature_prob': str(prob6), \
                   }
    print(result_data)
    return jsonify(result_data)

if __name__ == '__main__':
    app.run(debug=True)
