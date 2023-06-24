from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def index():
    return "MY FIRST MLPROJECT"
if __name__ == '__main__':
    app.run(debug = True)
    