from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/hello/<user>")
def hello_name(user):
    return render_template('templates/hello.html', name = user)

if __name__=="__main__":
    app.run(debug=True)