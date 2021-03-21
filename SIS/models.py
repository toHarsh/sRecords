from SIS import db,login_manager
from flask_login import UserMixin

# @app.before_first_request
# def create_tables():
#     db.create_all()

@login_manager.user_loader
def get_user(user_id):
    return Admin.query.get(int(user_id))

class Info(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    rollNo = db.Column(db.Integer,unique=True, nullable=False)
    prn = db.Column(db.Integer,unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    mobNo = db.Column(db.Integer,unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Info('{self.rollNo}','{self.prn}','{self.name}','{self.mobNo}','{self.email}','{self.city}','{self.state}')"

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Admin('{self.email}','{self.password}')"