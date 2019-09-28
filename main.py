from flask import Flask, render_template, redirect, url_for, request, jsonify, Response
from flask_cors import CORS
# Create the ap
# p object that will route our calls
app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
# Add a single endpoint that we can use for testing


@app.route('/', methods=['POST'])
def suyash():
    content = request.get_json()
    print("suyash", content)
    return "suyash"


# When run from command line, start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
