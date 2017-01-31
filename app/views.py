from app import app
from flask import render_template

@app.route("/secret")
def secret():
    user = {"nickname": "Boss"}
    return render_template('secret.html', title="secret", user=user)
@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Boss"}
    posts = [
            {
                'author': {'nickname': 'Rowlingmon'},
                'body': "Snape killed Dumbledore."
            },
            {
                'author': {'nickname': 'devmon'},
                'body': "You've git to commit everything, mate!"
            }
        ]
    return render_template('index.html', title="home", user=user, posts=posts)
