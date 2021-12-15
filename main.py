from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.debug = 'debug'


@app.route('/')
def indice():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
