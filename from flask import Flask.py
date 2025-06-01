from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Привет, Flask!"

@app.route("/about")
def about():
    return "Это страница о приложении Flask."

if __name__ == "__main__":
    app.run(debug=True)
