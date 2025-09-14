import uuid

class Article:

    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id', str(uuid.uuid4()))
        self._set_title(kwargs.get('title', None))
        self._set_description(kwargs.get('description', None))

    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    def _set_title(self, value):
        if not value:
            raise Exception('Article title must be set...')
        
        self._title = value

    @property
    def description(self):
        return self._description
    
    def _set_description(self, value):
        if not value:
            raise Exception('Article description must be set...')
        
        self._description = value