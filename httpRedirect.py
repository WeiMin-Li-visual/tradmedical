#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:03
# @Author  : zhibindeng
# @Email   : zhibindeng@shu.deu.cn
# @File    : http.py
# @Software: PyCharm

# 用于http重定向到https

from flask import Flask,redirect,request
app = Flask(__name__)


# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         url=request.url.replace('http://','https://',1)
#         return redirect(url,code=301)
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True)
