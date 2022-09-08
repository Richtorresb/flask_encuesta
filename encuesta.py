from crypt import methods
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def contador():
    return render_template("index.html")


@app.route('/enviar', methods=['POST'])
def enviar():
    print(request.form)
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentarios'] = request.form['comentarios']
    return redirect('/result')

@app.route('/result')
def resultado():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)