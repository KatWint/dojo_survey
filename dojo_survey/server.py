from flask import Flask, render_template, redirect, session, request, url_for
app = Flask(__name__)
app.secret_key = "off to the d0j0 world"

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/post', methods = ['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['loc']
    session['language'] = request.form['lang']
    session['comment'] = request.form['comment']
    return render_template('submit.html')

if __name__=="__main__":   
    app.run(debug=True)