from flask import Flask, render_template, redirect



app = Flask(__name__)
#Rutas generales :v

@app.route('/',  methods=["GET", "POST"])
def login():
    return render_template('Login.html')

@app.route('/Login', methods=["GET", "POST"])
def CerrarSesion():
    return login()



# LAYOUTS.. 
@app.route('/plantilla')
def layout():
    return render_template('layoutE.html' , methods=["GET"])

@app.route("/plantillaS")
def plantillaS():
    return render_template("layoutS.html")


@app.route("/plantillaD")
def plantilla():
    return render_template("layoutD.html")


# Aqui vienen las rutas de Estudiante.


@app.route('/Estudiante')
def Estudiante():
    return render_template('Estudiante/Estudiante.html' , methods=["GET"])
""" 
@app.route('/Estudiante/Matricularcursos' , methods=["GET", "POST"])
def Opcion1():
    return render_template('Estudiante/Cursos.html') """

@app.route('/Estudiante/actividades', methods=["GET"])
def Opion2():
    return render_template('Estudiante/actividades.html')

@app.route('/Estudiante/entregas', methods=["GET", "POST"])
def Opion3():
    return render_template('Estudiante/entregas.html')

@app.route('/Estudiante/perfil')
def Opion4():
    return render_template('Estudiante/perfil.html', methods=["GET", "POST"])

@app.route('/Estudiante/Calificaciones', methods=["POST"])
def Opion5():
    return render_template('Estudiante/Calificaciones.html')

@app.route('/Estudiante/novedades', methods=["POST"])
def Opion6():
    return render_template('Estudiante/novedades.html')

@app.route("/Estudiante/asignaturas/matricular", methods=["GET", "POST"])
def opcion7():
    return render_template("Estudiante/Asignaturas/Matricular.html")

@app.route("/Estudiante/asignaturas/materias",  methods=["GET", "POST"])
def Opcion8():
    return render_template("/Estudiante/asignaturas/MisMaterias.html")



#Rutas de Docente


@app.route('/Docente')
def Docente():
    return render_template('/Docente/Docente.html')


@app.route("/Docente/perfilD",  methods=["GET", "POST"] )
def PerfilD():
    return render_template("Docente/perfilD.html")

@app.route("/Docente/cursod" ,  methods=["GET"])
def CursoD():
    return render_template("Docente/CursoD.html")

@app.route("/Docente/Actividades/asignar" , methods=["GET", "POST"])
def AsignarTareas():
    return render_template("Docente/Actividades/asignar.html")

@app.route("/Docente/Actividades/Calificar", methods=["GET", "POST"] )
def CalificarTareas():
    return render_template("Docente/Actividades/Calificar.html")

@app.route("/Docente/Calendario")
def Calendario():
    return render_template("Docente/Calendario.html")


#Rutas SuperAdministrador


@app.route('/Administrador')
def logiS():
    return render_template('Administrador/Admin.html')

@app.route("/Administrador/PerfilS" , methods=["GET", "POST"])
def PerfilS():
    return render_template("Administrador/PerfilS.html")

@app.route("/Administrador/GestiondeCursos", methods=["GET", "POST"])
def GestiondeCursos():
    return render_template("Administrador/GestionCurso.html")

@app.route("/Administrador/CrearUsuarioRoles", methods=["GET", "POST"])
def CrearUsuarioR():
    return render_template("Administrador/CrearUaR.html")

@app.route("/Administrador/GestiondeUsuarios", methods=["GET", "POST"])
def GestiondeUsuarios():
    return render_template("Administrador/GestionUsuarios.html")

@app.route("/Administrador/VisualizarUsuarios", methods=["GET", "POST"])
def VisualizarUsuariosS():
    return render_template("Administrador/VisualizarUsuarios.html")

@app.route("/Administrador/CrearAsignatura", methods=["GET", "POST"])
def CrearAsignatura():
    return render_template("Administrador/CrearAsignatura.html")

@app.route("/Administrador/Calendario", methods=["GET", "POST"])
def CalendarioS():
    return render_template("Administrador/CalendarioS.html")

