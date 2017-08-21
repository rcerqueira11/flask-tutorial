from flask import render_template, url_for, request, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user

from thermos import app, db, login_manager
from forms import BookmarkForm, LoginForm
from models import User, Bookmark


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))

# @app.route('/add')
@app.route('/add', methods = ['GET','POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user= current_user, url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Sored bookmark '{}'".format(bm.description))
        return redirect(url_for('index'))
    return render_template('add.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)

# to use the 404 error page we use handler error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
# to use the 500 error page we use handler error
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       #login validate the user..
       user = User.get_by_username(form.username.data)
       if user is not None and user.check_password(form.password.data):
           login_user(user, form.remember_me.data)
           flash("Logged in successfully as {}.".format(user.username))
           return redirect(request.args.get("next") or url_for('user',username=user.username))
        #    request.args.get("next"): salva la pagina donde queriamos acceder para que cuando nos logueemos nos redirecione a dicha pagina
    flash("Incorrect username or password")
    return render_template("login.html", form=form)