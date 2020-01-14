# coding:utf-8

from flask import Flask, render_template, request, url_for, session, jsonify
import numeron


app = Flask(__name__)
app.secret_key = "test"


@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("mainpage.html")


@app.route("/soloplay", methods=["GET"])
def solo_play():
    session["rnd"] = numeron.get_random_num()
    return render_template("soloplay.html")


@app.route("/soloplay/evaluate", methods=["POST"])
def evaluate():
    answear = request.form["answear"]
    eat, bite = numeron.evaluate(answear, session.get("rnd"))
    result = {"answear": answear, "result": str(eat) + "E " + str(bite) + "B"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
