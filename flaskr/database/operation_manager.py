import os
import mariadb
from flaskr.database.query_manager import QueryManager
# from flaskr.database.model_manager import ModelManager

class OperationManager:
    '''
    This class is responsible for querying the db based on user actions. Main actions:
        - insert
        - update
        - delete
        - get
    '''

    # def __init__(self, query_manager=QueryManager(), model_manager=ModelManager()):
    #     self.query_manager = query_manager
    #     # self.model_manager = model_manager

    def __init__(self, query_manager=QueryManager()):
        self._query_manager = query_manager
        self._conn = None

    @property
    def query_manager(self):
        return self._query_manager
    
    def set_db_connection(self):
        try:
            self._conn = mariadb.connect(
                user=os.environ.get('USER', None),
                password=os.environ.get('PASS', None),
                host=os.environ.get('HOST', None),
                database=os.environ.get('DB', None)
            )
        except Exception as e:
            print(f"Couldn't connect to the Database: {str(e)}")
            raise
    
    @property
    def conn(self):
        return self._conn
    
    def close_db_connection(self):
        try:
            self.conn.close()
        except Exception as e:
            print(f"Couldn't close the DB connection: {str(e)}")
            raise

    