from app import db
from datetime import datetime


class Log(db.Model):

    __tablename__ = "log"

    log_id = db.Column("log_id", db.Integer, primary_key=True)
    response_data = db.Column("response_data", db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Log('{self.log_id}', '{self.response_data}', '{self.timestamp}')"
