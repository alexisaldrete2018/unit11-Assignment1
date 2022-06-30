from flask import Flask             # From the flask module import the Flask class

app = Flask(__name__)               #Create an instance of the Flask class into app
                                    #app is now an object

@app.get("/")                       #Flask decorator that allows us to map a route to a view function
def index():                        # Our view function
    return "<h1>Hello world!</h1>"  #Return statement


@app.get("/aboutme")
def get_about():
    me = {
        "first_name" : "Alexis",
        "last_name": "Aldrete",
        "hobbies": "Photo and Video creation",
        "active": True
    }
    return me