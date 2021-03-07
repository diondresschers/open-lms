from flask import Flask # We are importing this `Flask`-class.
app = Flask(__name__) # We are making an instanse called `app` of this `Flask`-class. With `__name__`, it is default Python and it knows where to look for static files and templates.

@app.route("/") # This is the route, this is a route decorator. The `route` is the method.
def hello():
    return("Hello World!")
