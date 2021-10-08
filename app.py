from flask import Flask, render_template, redirect

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('Login.html')
@app.route('/plantilla')
def layout():
    return render_template('layout.html')

@app.route('/Estudiante')
def Estudiante():
    return render_template('Estudiante/Estudiante.html')


@app.route('/Estudiante/Asignaturas')
def Admin2():
    return render_template('Estudiante/Estudiante.html')