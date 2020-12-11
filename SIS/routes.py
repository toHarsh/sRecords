from flask import render_template,url_for,flash,redirect,abort,request,Blueprint
from flask_login import current_user,login_user,logout_user,login_required
from SIS import app,db
from SIS.forms import sisForm,adminForm
from SIS.models import Info,Admin
from functools import wraps

sis = Blueprint('sis',__name__)

@sis.before_app_first_request
def create_tables():
    db.create_all()

@sis.route("/",methods=['GET','POST'])
@sis.route("/home",methods=['GET','POST'])
def home():
    form = sisForm()
    if form.validate_on_submit():
        student = Info(rollNo = form.rollNo.data,prn = form.prn.data,name = form.name.data,mobNo = form.mobNo.data,email = form.email.data,city = form.city.data,state = form.state.data)
        db.session.add(student)
        db.session.commit()
        flash(f'Submission Successful!','success')
        return redirect(url_for('sis.home'))

    return render_template('register.html',title="Student Information System",form=form)

@sis.route("/display",methods=['GET','POST'])
@login_required
def display():
    infos = Info.query.order_by(Info.rollNo)
    return render_template('display.html',title="Dahboard/Display",infos=infos)

@sis.route("/admin-register",methods=['GET','POST'])
def adminReg():
    form = adminForm()
    if form.validate_on_submit():
        Reg = Admin.query.filter_by(email=form.email.data,password=form.password.data).first()
        db.session.add(Reg)
        db.session.commit()
        return redirect(url_for('sis.adminLog'))
    else:
        flash(f'Submission Unsuccessful!','danger')  

    return render_template("adminRegister.html",title="Admin Register!",form=form)

@sis.route("/admin-login",methods=['GET','POST'])
def adminLog():
    form = adminForm()
    if form.validate_on_submit():
        Login = Admin.query.filter_by(email=form.email.data,password=form.password.data).first()
        if Login:
            login_user(Login)
            return redirect(url_for('sis.display'))
        else:
            flash(f"Wrong Credentials!",'danger')
    return render_template("adminLogin.html",title="Admin Login!",form=form)

@sis.route("/display/delete",methods=['GET','POST'])
def adminDel():
    delCard = Info.query.first()
    db.session.delete(delCard)
    db.session.commit()
    flash(f"Your Post has been deleted!","danger")
    return redirect(url_for('sis.display'))