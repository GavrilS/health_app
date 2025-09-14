import uuid

class Segment:

    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id', str(uuid.uuid4()))
        self._set_heading(kwargs.get('heading', None))
        self._set_description(kwargs.get('description', None))
        self._segment_order = kwargs.get('segment_order', 1)

    @property
    def id(self):
        return self._id
    
    @property
    def heading(self):
        return self._heading
    
    def _set_heading(self, value):
        if not value:
            raise Exception('Article segment heading is missing...')
        
        self._heading = value

    @property
    def description(self):
        return self._description
    
    def _set_description(self, value):
        if not value:
            raise Exception('Article segment description is missing...')
        
        self._description = value

    @property
    def segment_order(self):
        return self._segment_order