from flask import Flask,render_template,jsonify,request

app = Flask(__name__)


@app.route("/")
def index_page():
	return render_template("index.html")



app.run()
