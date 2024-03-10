from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome my Website to watch my boobies"
@app.route('/master')
def master():
    return "Good Morning Sir"



if __name__ == '__main__':
    app.run(debug=True)
