from app import db
from datetime import datetime
from app.models.users import User

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    todo = db.Column(db.String(64), nullable=False)

    describe = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return '<Todos {}>'.format(self.todo)