from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email,DataRequired,Length, ValidationError
from SIS.models import Info
import email_validator

class sisForm(FlaskForm):
    rollNo = StringField('Roll No',
                        validators=[DataRequired()])
    prn = StringField('Roll No',
                        validators=[DataRequired(),Length(min=9,max=10)])
    name = StringField('Name',
                        validators=[DataRequired(),Length(min=2,max=40)])
    mobNo = StringField('Mobile No',
                        validators=[DataRequired(),Length(min=9,max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    city = StringField('Name',
                        validators=[DataRequired(),Length(min=2,max=40)])
    state = StringField('Name',
                        validators=[DataRequired(),Length(min=2,max=40)])
    submit = SubmitField('Submit')

    def validate_rollNo(self,rollNo):
        info = Info.query.filter_by(rollNo=rollNo.data).first()
        if info:
            raise ValidationError('This Roll No is already there in the database.')
    
    def validate_prn(self,prn):
        info = Info.query.filter_by(prn=prn.data).first()
        if info:
            raise ValidationError('This PRN is already there in the database.')
    
    def validate_mobNo(self,mobNo):
        info = Info.query.filter_by(mobNo=mobNo.data).first()
        if info:
            raise ValidationError('This Mobile Number is already there in the database.')

    def validate_email(self,email):
        info = Info.query.filter_by(email=email.data).first()
        if info:
            raise ValidationError('This Email is already there in the database.')

    #def check_prn(self,prn):
    #    info = Info.query.filter_by(prn=prn.data).first()
    #    if len(prn) < 10:
    #        raise ValidationError('PRN must be of 10 digits')
    #        
    #def check_mobNo(self,mobNo):
    #    info = Info.query.filter_by(mobNo=mobNo.data).first()
    #    if len(mobNo) < 10:
    #        raise ValidationError('Mobile Number must be of 10 digits')