from flask import Flask,render_template,request,jsonify,json
# from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class

app = Flask(__name__)
import random
import time
import os
import cinfig

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/uploadImage',methods=['POST',"GET"])
def uploadImage():
    fn = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(0, 100) + '.png'
    image = request.files.get('image')
    pic_dir = os.path.join(cinfig.UPLOADED_PHOTOS_DEST, fn)
    print(pic_dir)
    image.save(pic_dir)

    return jsonify({'error':pic_dir})

# @app.route('/api/v/upload/<name>',methods=['POST','GET'])
# def mp_img(openid):
#
#
#     hash_openid = md5(openid)
#     new = compression_img(avata)
#     creat_folder(os.path.join(app.config['UPLOADS_FOLDER'], hash_openid))
#     pic_dir = os.path.join(app.config['UPLOADS_FOLDER'], hash_openid, fn)
#     new.save(pic_dir)
#     folder = photosSet.url(hash_openid)
# 	img_dir= folder + '/' + fn
#     return img_dir
#
#
# @app.route('/api/v/userinfo',methods=['POST'])
# def userinfo():
#     info = request.values.get('info')
#     appid = 'wx000000000032332'  //这里填你的appid
#     secret = 'jd82hhewh808b3sddada915e0b3' //你的secret_key
#     user_info = json.loads(info)
#     code = user_info['code']
#     url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
#     appid, secret, code)
#     data = requests.get(url).text
#     session_ = json.loads(data)
#     session_key = session_['session_key']
#     encryptedData = user_info['encryptedData']
#     iv = user_info['iv']
#     pc = WXBizDataCrypt(appid, session_key)
#     return pc.decrypt(encryptedData, iv)


if __name__ == '__main__':
    app.run(debug=True)
