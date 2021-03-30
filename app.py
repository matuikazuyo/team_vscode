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
    num = int(num)
    ensyu = num * 2 * 3.14
    menseki = num * num * 3.14
    return render_template("en2.html", ensyu=ensyu, menseki=menseki)

@app.route("/kyuuyo")
def ooo():
    return render_template("kyuuyo.html")


@app.route("/yyyyy")
def kyuuyo_calc():
    z = request.args.get("jikyuu")
    r = request.args.get("zikan")
    z = int(z)
    r = int(r)
    kyu = z * r
    return render_template("kyuuyo2.html", kyu=kyu)

if __name__ == "__main__":
    app.run(debug=True)