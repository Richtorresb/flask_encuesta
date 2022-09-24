from crypt import methods
from flask_app.models.user import Users
from flask import render_template,request, redirect, session, flash
from flask_app import app

@app.route('/')
def crear():
    usuarios = Users.get_all()
    return render_template("index.html", usuarios=usuarios)


@app.route('/enviar', methods=['POST'])
def enviar():
    if not Users.validate(request.form):
        flash("error al crear usuario", "error")
        # redirigir a la ruta donde se renderiza el formulario de burger
        return redirect('/')
    
    data={
        'nombre': request.form['nombre'],
        'ubicacion': request.form['ubicacion'],
        'idioma': request.form['idioma'],
        'comentario': request.form['comentarios'],
    }
    guardar = Users.save(data)
    flash("usuario creado correctamente", "success")
    return redirect(f'/result/{guardar}')

@app.route('/result/<id>')
def resultado(id):
    data={
        'id': int(id)
    }
    result = Users.seleccionar(data)
    result = result[0]
    return render_template("mostrar.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)