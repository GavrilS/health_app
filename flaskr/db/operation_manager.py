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
    
    def set_db_connection(self):
        try:
            self._conn = mariadb.connect(
                user=os.environ.get('DB_USER', None),
                password=os.environ.get('DB_PASS', None),
                host=os.environ.get('DB_HOST', None),
                database=os.environ.get('DB', None)
            )
            print('Connected to DB')
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
        cur = self._conn.cursor()
        cur.execute(query)
        self._conn.commit()
        return cur