from flask import Flask

'''
the app creates an instance for the flask
it is used for Web Server Gateway Interface(WSGI)
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course. This is an Amazing Course"
@app.route("/index")
def index():
    return "Welcome to Index page"

if __name__=="__main__":
    app.run(debug=True)