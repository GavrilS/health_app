import os
import mariadb


class OperationManager:
    '''
    This class is responsible for querying the db based on user actions. Main actions:
        - insert
        - update
        - delete
        - get
    '''
    def __init__(self):
        self._conn = None
    
    def _set_db_connection(self):
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

    def execute_query(self, query):
        self._set_db_connection()
        cur = self._conn.cursor()
        cur.execture()
        return cur