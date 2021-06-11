from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")

if __name__ == '__main__':
    app.run(debug=True)