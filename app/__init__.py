from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == '__name__':
    app.run(debug=True)