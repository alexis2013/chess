from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.debug = 'debug'


@app.route('/')
def indice():
    return render_template('index.html')


@app.route('/form-data', methods=['POST'])
def formulario():
    if request.method == 'POST':
        print(request)

    return url_for('/')


if __name__ == '__main__':
    app.run(debug=True)
