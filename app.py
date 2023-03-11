from flask import Flask,redirect, render_template, url_for
from flask import request
#from flask import url_for
import forms 
#from flask import jsonfly
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask (__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route("/",methods=['GET','POST'])
def index():
    create_forms=forms.UseForm(request.form)
    if request.method=='POST':
        alumn= Alumnos(nombre=create_forms.nombre.data,
                       apellidos=create_forms.apellidos.data,
                       email=create_forms.email.data)
        db.session.add(alumn)
        db.session.commit()
    return render_template('index.html',form=create_forms)

@app.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_forms=forms.UseForm(request.form)
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html',form=create_forms,alumnos=alumnos)

@app.route("/modificar",methods=['GET','POST'])
def modificar():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alumn1= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_forms.id.data=alumn1.id
        create_forms.nombre.data= alumn1.nombre
        create_forms.apellidos.data= alumn1.apellidos
        create_forms.email.data= alumn1.email

    if request.method=='POST':
        id=create_forms.id.data
        alumn= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn.id=create_forms.id.data
        alumn.nombre=create_forms.nombre.data
        alumn.apellidos=create_forms.apellidos.data
        alumn.email=create_forms.email.data
        db.session.add(alumn)
        db.session.commit()
        return redirect(url_for('ABCompleto'))

    return render_template('modificar.html',form=create_forms)

@app.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_forms=forms.UseForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alumn1= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_forms.id.data=alumn1.id
        create_forms.nombre.data= alumn1.nombre
        create_forms.apellidos.data= alumn1.apellidos
        create_forms.email.data= alumn1.email


    if request.method=='POST':
        id=create_forms.id.data
        alumn= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumn.id=create_forms.id.data
        alumn.nombre=create_forms.nombre.data
        alumn.apellidos=create_forms.apellidos.data
        alumn.email=create_forms.email.data
        db.session.delete(alumn)
        db.session.commit()
        return redirect(url_for('ABCompleto'))

    return render_template('eliminar.html',form=create_forms)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)