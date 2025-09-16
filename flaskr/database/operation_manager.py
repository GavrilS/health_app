from flaskr.database.query_manager import QueryManager

class OperationManager:
    '''
    This class is responsible for querying the db based on user actions. Main actions:
        - insert
        - update
        - delete
        - get
    '''

    def __init__(self, query_manager=QueryManager()):
        self.query_manager = query_manager