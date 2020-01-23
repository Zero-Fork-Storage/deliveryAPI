from flask import Flask, render_template
from app import tracking_bot


app = Flask(__name__)
app.register_blueprint(tracking_bot)

@app.route('/', methods=['GET'])
def HelloApi():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)