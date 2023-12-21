from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    username = db.Column(db.String(64), index=True, unique=True)

    email = db.Column(db.String(120), index=True, unique=True)

    password = db.Column(db.String(128))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    update_at = db.Column(db.DateTime, default=datetime.utcnow)


    def hashPassword(self,password):
        self.password = generate_password_hash(password)


    def checkPassword(self,password):
        return check_password_hash(self.password, password)

        
    def __repr__(self):
        return '<User {}>'.format(self.username)
    

