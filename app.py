from flask import Flask
import flask

app=Flask(__name__)

@app.route('/')
def holamundo():
    return "<p>hola mundo</p>"

if __name__ =='__main__':
    app.run(port=3500,debug=True )