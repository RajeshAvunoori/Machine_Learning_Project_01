from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def index():
    print('HI')
    return "MY FIRST MLPROJECT"
if __name__ == '__main__':
    app.run()
    