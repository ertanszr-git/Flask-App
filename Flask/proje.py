from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
    return "<h1>Welcome, {}!<h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
