from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime

# from logging import DEBUG
app = Flask(__name__)
# app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\x05\xa5\xa6\xb8\xe8\x06\x0f\xa9\x98\xf4\xf8\xe5H\x92j9\xab\x16\xe5\xe0\xa8\x9e\xb9\x92'
bookmarks = []

def store_bookomark(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse = True)[:num]



# class User:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def initials(self):
#         return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    # return "Hello World!"
    # return render_template('index.html', title="Title passed form view to template" ,text="Text passed from view to template")
    # return render_template('index.html', title="Title passed form view to template" ,user=User("Reindert-Jan","Errk"))
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

# @app.route('/add')
@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookomark(url)
        # app.logger.debug('sored url: '+ url)
        flash("Sored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

# to use the 404 error page we use handler error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
# to use the 500 error page we use handler error
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
#   app.run(host:'127.0.0.1', port=8000, debug=True)
#   app.run()
    # debug mode
    app.run(debug=True)
 