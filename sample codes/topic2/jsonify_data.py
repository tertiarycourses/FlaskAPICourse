from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API.')

if __name__ == '__main__':
     app.run(debug=True)