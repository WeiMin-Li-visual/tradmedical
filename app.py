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

    return jsonify({'error':pic_dir})

if __name__ == '__main__':
    app.run(debug=True)
