from flaskr.database.query_manager import QueryManager
from flaskr.database.model_manager import ModelManager

class OperationManager:
    '''
    This class is responsible for querying the db based on user actions. Main actions:
        - insert
        - update
        - delete
        - get
    '''

    def __init__(self, query_manager=QueryManager(), model_manager=ModelManager()):
        self.query_manager = query_manager
        self.model_manager = model_manager