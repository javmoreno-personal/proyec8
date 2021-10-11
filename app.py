from flask import Flask, render_template, redirect


app = Flask(__name__)
#Rutas generales :v

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/Login')
def CerrarSesion():
    return login()

# Aqui vienen las rutas de Estudiante.
@app.route('/plantilla')
def layout():
    return render_template('layoutE.html')

@app.route('/Estudiante')
def Estudiante():
    return render_template('Estudiante/Estudiante.html')

@app.route('/Estudiante/cursos')
def Opcion1():
    return render_template('Estudiante/Cursos.html')

@app.route('/Estudiante/actividades')
def Opion2():
    return render_template('Estudiante/actividades.html')

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

#Rutas de Docente


@app.route('/Docente')
def Docente():
    return render_template('/Docente/Docente.html')

@app.route("/plantillaD")
def plantilla():
    return render_template("layoutD.html")

@app.route("/Docente/perfilD")
def PerfilD():
    return render_template("Docente/perfilD.html")

@app.route("/Docente/cursod")
def CursoD():
    return render_template("Docente/CursoD.html")

@app.route("/Docente/Actividades/revisar")
def AsignarTareas():
    return render_template("Docente/Actividades/asignar.html")

@app.route("/Docente/Actividades/Calificar")
def CalificarTareas():
    return render_template("Docente/Actividades/Calificar.html")

@app.route("/Docente/Calendario")
def Calendario():
    return render_template("Docente/Calendario.html")


#Rutas SuperAdministrador


@app.route('/Administrador')
def logiS():
    return render_template('Administrador/Admin.html')

@app.route("/plantillaS")
def plantillaS():
    return render_template("layoutS.html")

@app.route("/Administrador/PerfilS")
def PerfilS():
    return render_template("Administrador/PerfilS.html")

@app.route("/Administrador/GestiondeCursos")
def GestiondeCursos():
    return render_template("Administrador/GestionCurso.html")

@app.route("/Administrador/CrearUsuarioRoles")
def CrearUsuarioR():
    return render_template("Administrador/CrearUaR.html")

@app.route("/Administrador/GestiondeUsuarios")
def GestiondeUsuarios():
    return render_template("Administrador/GestionUsuarios.html")

@app.route("/Administrador/VisualizarUsuarios")
def VisualizarUsuariosS():
    return render_template("Administrador/VisualizarUsuarios.html")

@app.route("/Administrador/CrearAsignatura")
def CrearAsignatura():
    return render_template("Administrador/CrearAsignatura.html")

@app.route("/Administrador/Calendario")
def CalendarioS():
    return render_template("Administrador/CalendarioS.html")

