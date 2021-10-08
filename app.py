from flask import Flask, render_template, redirect

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('Login.html')


@app.route('/plantilla')
def layout():
    return render_template('layoutE.html')

@app.route('/Estudiante')
def Estudiante():
    return render_template('Estudiante/Estudiante.html')


@app.route('/Estudiante/Cursos')
def Opcion1():
    return render_template('Estudiante/Cursos.html')

@app.route('/Estudiante/activiades')
def Opion2():
    return render_template('Estudiante/actividades.html.html')

@app.route('/Estudiante/entregas')
def Opion3():
    return render_template('Estudiante/entregas.html')

@app.route('/Estudiante/perfil')
def Opion4():
    return render_template('Estudiante/perfil.html')

@app.route('/Estudiante/asignaturas')
def Opion5():
    return render_template('Estudiante/asignaturas.html')

@app.route('/Estudiante/novedades')
def Opion6():
    return render_template('Estudiante/novedades.html')



@app.route('/Estudiante/CerrarSesion')
def Opion7():
    return render_template('Login.html')
     