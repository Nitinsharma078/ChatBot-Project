from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome my Website"
def master():
    return "Home is comning !!"




if __name__ == '__main__':
    app.run(debug=True)
