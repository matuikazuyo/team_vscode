from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/en")
def en():
    return render_template("en.html")

@app.route("/en_calc")
def en_calc():
    num = request.args.get("num")
    ensyu = num * 2 * 3.14
    menseki = num * num * 3.14
    return render_template("en2.html", ensyu=ensyu, menseki=menseki)

if __name__ = "__main__":
    app.run(debug=True)