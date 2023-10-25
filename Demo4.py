from flask import Flask
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return 'Hello Admin Sir!!'

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "hello %s you logged in as guest user" % guest

@app.route("/usr/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
    app.run(debug = True)
