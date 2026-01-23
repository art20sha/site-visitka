from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    uid = request.form["uid"]
    msg = request.form["msg"]

    users = load_users()
    users[uid] = {"msg": msg, "reply": ""}

    with open("users.json", "w") as f:
        json.dump(users, f)

    return "ok"

@app.route("/reply/<uid>")
def reply(uid):
    users = load_users()
    return jsonify(users.get(uid, {}))

if __name__ == "__main__":
    app.run(debug=True)
