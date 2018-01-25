from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="" method="POST">
            <label>Rotate By:
            <input type="text" name="rot" value="0"></label><br><br>
            <label>Words to Rotate</label>
            <textarea name="text"></textarea><br>
            <input type="submit" />
        </form>
    </body>
</html>"""
@app.route("/")
def index():
    return "Hello World"

@app.route("/",  methods=['POST'])
def index():
    return form
def encrypt(rotation_num, rotate_string):
    return """<h1></h1>"""


app.run(host='0.0.0.0')