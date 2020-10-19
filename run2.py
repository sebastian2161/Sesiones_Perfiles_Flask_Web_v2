from flask import *
from functools import wraps
import sqlite3
import time
import pandas as pd
from flask import session



DATABASE = 'dataweb.db'

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect('dataweb.db')
    cursor = con.cursor()
    print('La base funcionò bien')

def run_query(query='',parameters=()):
    conn = sqlite3.connect('dataweb.db')
    cursor = conn.cursor()                 # Crear un cursor
    cursor.execute(query, parameters)                  # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
       data= cursor.fetchall()               # Traer los resultados de un select
       
    else:
        conn.commit()                          # Hacer efectiva la escritura de datos
        data = None
         
    #cursor.close()                         # Cerrar el cursor
    #conn.close()                           # Cerrar la conexión
    #conn.close()                           # Cerrar la conexión
    
    return data





@app.route('/')
def index():

    #query = 'SELECT * FROM datosclientes'
    #curs  = run_query(query)
    #return render_template('index_desa.html', contacts = curs)
     return render_template('layout1.html')
     

@app.route('/Login')
def crear():
    return render_template('crear.html')

@app.route('/crear_datos', methods = ['POST'])
def crear_datos():
      
    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']

        query1 = "SELECT * FROM datosclientes WHERE fullname ='%s' and email ='%s'" % (fullname,email)
        result1 = run_query(query1)
        #print(result1)
        
        if result1:
            result2 = list(result1[0])
        #print(result2[0])  
        
        if result1:
            #flash ('Existe El Contacto:'+ result2[0])
            session['username'] = result2[0]
            session['rol'] = result2[2]
            session['item_crear'] = ''
            session['item_modificar'] = ''
            session['item_eliminar'] = ''
            session['item_consultar'] = ''
            session['item_grafico'] = ''

            #print(session)
            
            query1 = "SELECT fullname, rol,item_menu, activo, checkbox from perfil_usuario  WHERE fullname ='%s' and activo = 'SI' order by id_item_menu" % (result2[0])
            result3 = run_query(query1)
            print(result3)

            for z in result3:
                if z[2] == 'crear':
                    session['item_crear'] = z[2]
                if z[2] == 'modificar':
                    session['item_modificar'] = z[2]
                if z[2] == 'eliminar':
                    session['item_eliminar'] = z[2]
                if z[2] == 'consultar':
                    session['item_consultar'] = z[2]
                if z[2] == 'grafico':
                    session['item_grafico'] = z[2]
                
            #print(session['item_crear'])
            #print(session['item_modificar'])
            #print(session['item_eliminar'])
            #print(session['item_consultar'])
            #print(session['item_grafico'])


            #return 'Nombre Usuario: ' + session['username'] + '---'+session['rol']
            return render_template('layout2.html')
        else:
            return 'No existe el contacto, crear una cuenta de usuario'


@app.route('/perfiles_usuarios')
def perfiles_usuarios():

    query = 'SELECT fullname, rol,item_menu, checkbox from perfil_usuario  order by id_item_menu'
    curs  = run_query(query)

    return render_template('index_desa.html', contacts = curs)

@app.route('/enviar')
def enviar():

            query = "SELECT fullname, rol,item_menu, checkbox from perfil_usuario  order by id_item_menu " 
            result = run_query(query)

            user = request.args.get('user', 'all')
            print(user)

            nombre = []
            nombre1 = request.args
            nombre2 = list(nombre1)

            
            for x1 in nombre2:
                nombre.append(x1)

            print(nombre)
            print(result)

            for x2 in result:
                if x2[2] in nombre:
                    #print('Marcar checkbox:'+x2[2])
                    query = "UPDATE perfil_usuario SET checkbox = 'checked=checked', activo = 'SI' WHERE fullname  ='%s' and item_menu='%s'" % (user, x2[2])
                    result_v1 = run_query(query)
                else:
                    #print('Marcar no checkbox:'+x2[2])
                    query = "UPDATE perfil_usuario SET checkbox = '', activo = 'NO' WHERE fullname  ='%s' and item_menu='%s'" % (user,x2[2])
                    result_v1 = run_query(query)
                    #print('Desmarcar:'+x2[0])
            
            #flash ('Seleccion de items actualizados exitosamente')
            return render_template('index_desa2.html')
            
if __name__ == '__main__':
    app.run(port = 3000, debug=True)





#connect_db()
#index()
#run_query()