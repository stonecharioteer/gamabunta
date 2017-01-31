from app import app

from flask import render_template, flash, redirect

from .forms import LoginForm


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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid,data, str(form.remember_me.data)))
        return redirect('/index')
        
    return render_template('login.html', title='Sign In', form=form)

