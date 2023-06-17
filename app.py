from flask import Flask
### WSGI Application

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the world of Kaustubh"

if __name__== '__main__':
    app.run(debug=True)