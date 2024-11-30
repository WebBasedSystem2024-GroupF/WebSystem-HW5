from flask import Flask, render_template
import os

app = Flask(__name__)

# Root route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def resultPage():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
