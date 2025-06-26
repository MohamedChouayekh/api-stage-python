from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "API de démo pour mon stage !"

if __name__ == '__main__':
    app.run()
