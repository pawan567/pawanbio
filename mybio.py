"""
sample flask app for my bio
"""

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def mybio():
    "mybio page"
    return render_template('mybio.html',title='pawanbio')

#---START
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
