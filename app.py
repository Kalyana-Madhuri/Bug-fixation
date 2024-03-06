from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST","GET"])
def index():
    note = request.args.get("note")
    if note:
        notes.append(note)
    return render_template("home1.html", notes=notes)


if __name__ == '__main__':
     app.run(debug=True)