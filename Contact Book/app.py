from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/")
def main():
    with open("contacts.json") as f:
        jsondata = json.load(f)
    return jsonify(jsondata)

if __name__ == "__main__":
    app.run(debug=True)