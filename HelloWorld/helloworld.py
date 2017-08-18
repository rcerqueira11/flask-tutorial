from flask import Flask 

# flask constructor
app = Flask(__name__) 


@app.route('/index')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()