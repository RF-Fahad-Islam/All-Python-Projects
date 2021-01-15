from flask import Flask, jsonify
import json
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/prime/<int:n>")
def primeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
        else:
            prime = True

    if prime:
        result = {
            "Number": n,
            "Prime": True,
            "Server IP": "http://127.0.0.1:5000/"
        }
        print(f"The number {n} is Prime")
        return jsonify(result)
    else:
        result = {
            "Number": n,
            "Prime": False,
            "Server IP": "http://127.0.0.1:5000/"
        }
        print(f"The number {n} is not Prime")
        return jsonify(result)


@app.route("/api")
def currency_api():
    with open("news.json") as f:
        api = json.loads(f.read())
        return jsonify(api)


if __name__ == "__main__":
    app.run(debug=True)
