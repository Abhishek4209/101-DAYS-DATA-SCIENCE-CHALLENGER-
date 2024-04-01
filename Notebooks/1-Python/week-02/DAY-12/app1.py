from flask import Flask


app=Flask(__name__)






@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test2')
def test2():
    data=request.args.get('x')
    return "this is a data input form my url {}".format(data) 






if __name__ == '__main__':
    app.run(debug=True)



