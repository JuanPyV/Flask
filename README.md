# Flask: Equipo 7

- Based from: https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask


- Create environment (*optional*)
```bash
> mkdir myproject
> cd myproject
> py -3 -m venv venv
```

- Install pip
```bash
$ pip install Flask
```

- Hello world example from: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
```bash
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
```

