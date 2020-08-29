from SIS import db

class Info(db.Model):
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