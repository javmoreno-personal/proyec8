from flask import Flask, render_template as render, request, redirect, session, flash # Riderec / reques y url for son para redireccionamineto y session es para cerrar las sesiones. :v
#from flask_mysqldb import MySQL, MySQLdb  # Pip install Flask-MySQLdb


# Conexion con la base de datos :v

app = Flask(__name__)
app.secret_key = 'Equipo8'

   
#Rutas generales :v

@app.route('/Login', methods=["GET", "POST"])
def Login():
    return render("Login.html")
    
# LAYOUTS.. 
""" @app.route('/plantilla')
def layout():
    return render('layoutE.html')

@app.route("/plantillaS" )
def plantillaS():    
    return render("layoutS.html")


@app.route("/plantillaD")
def plantilla():
    return render("layoutD.html")
 """

# Aqui vienen las rutas de Estudiante.


@app.route('/Estudiante')
def Estudiante():
    return render('Estudiante/Estudiante.html' , methods=["GET"])
""" 
@app.route('/Estudiante/Matricularcursos' , methods=["GET", "POST"])
def Opcion1():
    return render('Estudiante/Cursos.html') """

@app.route('/Estudiante/actividades', methods=["GET"])
def Opion2():
    return render('Estudiante/actividades.html')

@app.route('/Estudiante/entregas', methods=["GET", "POST"])
def Opion3():
    return render('Estudiante/entregas.html')

@app.route('/Estudiante/perfil')
def Opion4():
    return render('Estudiante/perfil.html', methods=["GET", "POST"])

@app.route('/Estudiante/Calificaciones', methods=["GET","POST"])
def Opion5():
    return render('Estudiante/Calificaciones.html')  # Notas y promedios por materias v

@app.route('/Estudiante/novedades', methods=["GET","POST"])
def Opion6():
    return render('Estudiante/novedades.html')

@app.route("/Estudiante/asignaturas/matricular", methods=["GET", "POST"]) # Matricular materias 
def opcion7():
    return render("Estudiante/Asignaturas/Matricular.html")

@app.route("/Estudiante/asignaturas/materias",  methods=["GET", "POST"]) # Lista materias matriculadas
def Opcion8():
    return render("/Estudiante/asignaturas/MisMaterias.html")



#Rutas de Docente


@app.route('/Docente' , methods=["GET"])
def Docente():
    return render('/Docente/Docente.html')


@app.route("/Docente/perfilD",  methods=["GET", "POST"] )
def PerfilD():
    return render("Docente/perfilD.html")

@app.route("/Docente/cursod" ,  methods=["GET"])
def CursoD():
    return render("Docente/CursoD.html")

@app.route("/Docente/Actividades/asignar" , methods=["GET", "POST"])
def AsignarTareas():
    return render("Docente/Actividades/asignar.html")

@app.route("/Docente/Actividades/Calificar", methods=["GET", "POST"] )
def CalificarTareas():
    return render("Docente/Actividades/Calificar.html")

@app.route("/Docente/novedades" , methods=["GET"])
def Calendario():
    return render("Docente/novedades.html")


#Rutas SuperAdministrador


@app.route('/Administrador' , methods=["GET"])
def logiS():
    return render('Administrador/Admin.html')

@app.route("/Administrador/PerfilS" , methods=["GET", "POST"])
def PerfilS():
    return render("Administrador/PerfilS.html")

@app.route("/Administrador/GestiondeCursos", methods=["GET", "POST"]) # 
def GestiondeCursos():
    return render("Administrador/GestionCurso.html")

@app.route("/Administrador/CrearUsuarios", methods=["GET", "POST"])
def CrearUsuarioR():
    return render("/Administrador/GestionUsuarios/CrearUsuario.html")



""" @app.route("/Administrador/GestiondeUsuarios", methods=["GET", "POST"])
def GestiondeUsuarios():
    return render("Administrador/GestionUsuarios.html")
    
 """


@app.route("/Administrador/VisualizarUsuarios", methods=["GET", "POST"])
def VisualizarUsuariosS():
    return render("Administrador/GestionUsuarios/VisualizarUsuarios.html")

@app.route("/Administrador/CrearAsignatura", methods=["GET", "POST"])
def CrearAsignatura():
    return render("Administrador/CrearAsignatura.html")

@app.route("/Administrador/novedades", methods=["GET", "POST"])
def novedades():
    return render("Administrador/novedades.html")


@app.route("/Administrador/Calendario", methods=["GET", "POST"])
def CalendarioSS():
    return render("Administrador/calendario.html")




@app.route("/hacer_login", methods=["POST"])
def hacer_login():
    username =  request.form.get("username", None)
    txtPassword =  request.form.get("txtPassword", None)
    # Aquí comparamos. Lo hago así de fácil por simplicidad
    # En la vida real debería ser con una base de datos y una contraseña hasheada
    if username == "Equipo8" or username == "Admin2" and txtPassword == "Admin**123" or txtPassword == "Admin**456":
        # Si coincide, iniciamos sesión y además redireccionamos
        session["usuario"] = username
        # Aquí puedes colocar más datos. Por ejemplo
        #session["nivel"] = "administrador"
        return redirect("/Administrador")
    else:
        # Si NO coincide, lo regresamos
        flash("Usuario o Contraseña Incorrectos")
        return redirect("/Login")


# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/Login")


# Un "middleware" que se ejecuta antes de responder a cualquier ruta. Aquí verificamos si el usuario ha iniciado sesión
@app.before_request
def antes_de_cada_peticion():
    ruta = request.path
    # Si no ha iniciado sesión y no quiere ir a algo relacionado al login, lo redireccionamos al login
    if not 'usuario' in session and ruta != "/Login" and ruta != "/hacer_login" and ruta != "/logout" and not ruta.startswith("/static/Administrador"):
        flash("Inicia sesión para continuar")
        return redirect("/Login")
    # Si ya ha iniciado, no hacemos nada, es decir lo dejamos pasar
    
if __name__ == "__main__":
    app.run(debug=True) 