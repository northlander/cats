from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def cats():
    return jsonify(["Devon Rex", "Korat", "Manx", "Savannah", "Siberian", "Angora"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0',port=port)