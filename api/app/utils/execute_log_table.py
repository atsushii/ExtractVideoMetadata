from app import db
from app.models.models import Log


class ExecuteLogTable():

    def store_log(self, log_data):
        log = Log(response_data=str(log_data))
        db.session.add(log)
        db.session.commit()
