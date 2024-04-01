from flask import Flask,render_template,request,jsonify


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "this is index page"



@app.route('/test1')
def test1():
    return "this is test function"




if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)