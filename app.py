from flask import Flask, render_template
proj = Flask(__name__)
@proj.route('/test')
def index():
    return "Welcome to Infy Events !"

@proj.route('/user/<name>')
def myName(name):
    return render_template('user.html',fullName=name)

@proj.route('/add/<int:a>/<int:b>')
def addNum(a,b):
    return str(a+b)

@proj.route('/home')
def home():
    return """

                <!DOCTYPE HTML>
                <head>
                       Demo page</br>
                <title> Sample </title>
                </head>
                <body>
                Hello "Narendra"</br>
                Krishna is inviting you the farewell party</br>
                Join and have fun !!!</br>
                </body>
                </html>
    """


@proj.route('/demo')
def newPage():
    return render_template('sample.html')