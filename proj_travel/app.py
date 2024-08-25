from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def basic():
    return render_template("main_page.html")

@app.route('/index')
def index():  # put application's code here
    # return 'Hello World!'
    return render_template("index.html")

@app.route('/temp')
def temp():
    return render_template("temp.html")

if __name__ == '__main__':
    app.run(debug=True)
