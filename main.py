from flask import Flask
from flask import render_template
from flask import url_for
import random

app = Flask(__name__)

@app.route("/") #wenn diese URL aufgerufen wird, soll etwas passieren
def hello():


    foo = ['Syd', 'Gian', 'Silboi', 'Furk', 'Herrez']
    name_choice = random.choice(foo)
    about_link = url_for("about")
    return render_template("index.html", name=name_choice, link=about_link)

@app.route("/about")
def about():
    return "<h1>About Test <\h1>"
if __name__ == "__main__":
    app.run(debug=True, port=5000)
