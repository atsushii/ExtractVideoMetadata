from app import db
from app.models.models import Log


class ExecuteLogTable():
    """ 
    Execute log table.
    """

    def store_log(self, log_data):
        """
        Store return data for any API request and timestamp to log table.
        :param log_data: return data for any API request
        """
        log = Log(response_data=str(log_data))
        db.session.add(log)
        db.session.commit()
