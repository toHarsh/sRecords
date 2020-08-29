from flask import render_template,url_for,flash,redirect,abort,request
from SIS import app,db
from SIS.forms import sisForm
from SIS.models import Info
from functools import wraps


def sort_db(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        info_list = []
        info = Info.query.all()
        for i in info:
            info_list.append(i)

@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home():
    form = sisForm()
    if form.validate_on_submit():
        student = Info(rollNo = form.rollNo.data,prn = form.prn.data,name = form.name.data,mobNo = form.mobNo.data,email = form.email.data,city = form.city.data,state = form.state.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('display'))

    return render_template('register.html',title="Student Information System",form=form)

@app.route("/display",methods=['GET','POST'])
def display():
    infos = Info.query.order_by(Info.rollNo)
    return render_template('display.html',title="Student Display",infos=infos)

@app.route("/info/<int:info_id>")
def infoPage(info_id):
    info = Info.query.get_or_404(info_id)
    return render_template('info.html', title=info.title, info=info)

@app.route("/info/<int:info_id>/delete",methods=['POST'])
def delete_record(info_id):
    info = Info.query.get_or_404(info_id)
    
    db.session.delete(info)
    db.session.commit()
    return redirect(url_for('display'))