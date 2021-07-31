from flask import Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login',methods=['POST',"GET"])
def login():
    print(request.data)
    return jsonify({'status':True})

if __name__ == '__main__':
    app.run(debug=True)
