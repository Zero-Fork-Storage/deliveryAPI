from flask import Flask
from app import tracking_bot


app = Flask(__name__)
app.register_blueprint(tracking_bot)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)