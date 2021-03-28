from flask import Flask, render_template
from titulos import title1, titulo1

app = Flask(__name__)

verdad = True
puerto = 1717


@app.route('/')
def layout():
    return render_template("index.html", title1=title1, titulo1=titulo1)


if __name__ == '__main__':
    app.run(debug=verdad, port=puerto)
