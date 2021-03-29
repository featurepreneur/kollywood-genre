from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def hello_world():
    return render_template("index.html")






if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port="5000")

