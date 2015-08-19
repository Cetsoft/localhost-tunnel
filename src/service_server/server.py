from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route("/")
def main():
	return "Hello World"

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
	app.run()