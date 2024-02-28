from flask import Flask, render_template, request, redirect
from funciones import sec, second, hora
import random
app = Flask(__name__) #Para crear urls, puede ser app o cualq otro nombre, es una variable para guardar el objeto que devuelve Flask

@app.route("/") #Ruta para la pag principal
def home():
    return render_template("index.html") #Devuelve la plantilla

@app.route("/redirect")
def links():
    l1= "https://www.youtube.com/watch?v=Rk1MYMPDx3s&ab_channel=iTMG"
    l2= "https://www.youtube.com/watch?v=E6UGrULiwMQ&ab_channel=Muddbicc"
    l3= "https://www.youtube.com/watch?v=eY52Zsg-KVI&ab_channel=JulianJapenga"
    l4= "https://www.youtube.com/watch?v=F3YH-bo-E8I"
    l5="https://youtu.be/92ydUdqWE1g?t=27"
    l6="https://youtu.be/X8Nc8RCLy1s?t=85"
    l7="https://youtu.be/rvrZJ5C_Nwg?t=139"
    l8="https://youtu.be/NUYvbT6vTPs?t=1"
    link = [l1,l2,l3,l4,l5,l6,l7,l8]
    return redirect(random.choice(link))

@app.route("/datos", methods= ["POST", "GET"]) 
def datos():
    return render_template("conversor1.html")

@app.route("/ingrese_numero", methods= ["POST", "GET"]) 
def numero():
    return render_template("tablas.html")


@app.route("/tablas", methods= ["GET", "POST"]) 
def tablas():
    numero = request.form.get('number',type=int)
    return render_template("resultadoTabla.html", num=numero)

@app.route('/conversor1', methods=["POST","GET"])
def conversor():
    if request.form['submit'] == 'minseg': # Entre [] va el value del html
        if request.form['minutos'] == "":
            minuto = 0
            seg = request.form.get('segundos',type=int)
            titulo = "Segundos --> Minutos y Segundos"
        elif request.form['segundos'] == "":
            seg = 0
            minuto = request.form.get('minutos',type=int)
            titulo = "Minutos --> Minutos y Segundos"
        else:
            minuto = request.form.get('minutos', type=int)
            seg = request.form.get('segundos',type=int)
            titulo = "Minutos y Segundos --> Minutos y Segundos"
        m,s = second(minuto, seg)
        return render_template("resultado.html", titulo=titulo, unidad=f"{m} Minutos y {s} Segundos")
    elif request.form['submit'] == 'seg':
        if request.form['minutos'] == "":
            minuto = 0
            seg = request.form.get('segundos', type=int)
            titulo = "Segundos ---> Segundos"
        elif request.form['segundos'] == "":
            minuto = request.form.get('minutos',type=int)
            seg = 0
            titulo = "Minutos ---> Segundos"
        else:
            minuto = request.form.get('minutos', type=int)
            seg = request.form.get('segundos',type=int)
            titulo = "Minutos y Segundos ---> Segundos"
        s = sec(minuto, seg)
        return render_template("resultado.html", titulo=titulo, unidad=f"{s} Segundos")
    else:
        if request.form['submit'] == 'horaminseg':
            if request.form['minutos'] == "":
                minuto = 0
                seg = request.form.get('segundos', type=int)
                titulo = "Segundos ---> Horas, Minutos y Segundos"  
            elif request.form['segundos'] == "":
                minuto = request.form.get('minutos',type=int)
                seg = 0   
                titulo = "Minutos ---> Horas, Minutos y Segundos"
            else:
               minuto = request.form.get('minutos', type=int)
               seg = request.form.get('segundos',type=int) 
               titulo = "Minutos y Segundos ---> Horas, Minutos y Segundos"
            ho, mi, se = hora(minuto,seg)
            return render_template("resultado.html", titulo=titulo, unidad=f"{ho} Horas, {mi} Minutos y {se} Segundos")


if __name__ == "__main__":
    app.run(debug=True) #Para no tener que reiniciar el servidor a cada rato, se pone debug=True(significa que es de prueba)


#Para ejecutarlo: 
#1- Abrir consola de W. Poner cdm
#2- cd desktop (C:\Users\romin>cd desktop)
#3- cd Python Website (C:\Users\romin\Desktop>cd Python Website)
#4- python index.py (C:\Users\romin\Desktop\Python Website>python index.py)

