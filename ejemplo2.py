from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run()

# When running go to the URL http://127.0.0.1:5000/hello/<yourname>
