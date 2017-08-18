from flask import Flask, render_template, url_for
app = Flask(__name__)

class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    # return "Hello World!"
    # return render_template('index.html', title="Title passed form view to template" ,text="Text passed from view to template")
    return render_template('index.html', title="Title passed form view to template" ,user=User("Reindert-Jan","Errk"))

@app.route('/add')
def add():
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
 