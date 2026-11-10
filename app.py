from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    home = request.form("Home Team")
    away = request.form("Away Team")
    return home + " vs " + away

if __name__ == "__main__":
    app.run(debug=True)