from flask import (Flask, redirect, redirect, 
                    url_for, render_template, session)

app = Flask(__name__)   

@app.route('/')
def index():
    role = ''
    return render_template('index.html', role=role)

app.run(debug=True)    