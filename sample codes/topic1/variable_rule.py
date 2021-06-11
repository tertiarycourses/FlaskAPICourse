from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<username>')
def user(username):
    return 'Hello {}'.format(username)

@app.route('/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath {}'.format(subpath)

if __name__ == "__main__":
    app.run(debug=True)