
from flask import Flask, render_template, request

app = Flask(__name__)


# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    """This is the method that when the user enters the website will run
    index.html is the html file that contains a form asking for username and password of instagram account
    when the user presses ok button the scrapper script will run with the username and password and the results.html
    will be shown"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        return render_template("results.html", username=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)