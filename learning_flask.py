from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route('/home', methods =["POST", "GET"])
def home():
    return render_template("secondpage.html")
if __name__ == "__main__":
    app.run(debug=True)

