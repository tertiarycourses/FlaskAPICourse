from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/aboutus')
def blog():
    return 'About Us'

@app.route('/blog/post/<int:id>')
def post(id):
    return 'Blog Post {}'.format(id)

if __name__ == "__main__":
    app.run(debug=True)