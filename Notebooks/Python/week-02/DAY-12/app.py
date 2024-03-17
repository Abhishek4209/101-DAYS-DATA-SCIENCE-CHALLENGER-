from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/hellow1')
def hello_world1():
    return 'Hello, World!'





@app.route('/hellow2')
def hello_world2():
    return 'Hello, World!'





@app.route('/test')
def test():
    return 'this is my function to run app'






if __name__ == '__main__':
    app.run(debug=True)
