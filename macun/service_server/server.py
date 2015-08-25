from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from basicauth import requires_auth
from apiauth import requires_keyauth


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
@requires_auth
def main():
    return "Hello World"


@app.route("/key")
@requires_keyauth
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run()
