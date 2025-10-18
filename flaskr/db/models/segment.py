import uuid

class Segment:
    '''
    This class is a holder for a single article segment's attributes.
    '''

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
        '''
        Set heading only upon initialization. Heading is a required attribute!
        '''
        if not value:
            raise Exception('Article segment heading is missing...')
        
        self._heading = value

    @property
    def description(self):
        return self._description
    
    def _set_description(self, value):
        '''
        Set description only upon initialization. It is a required attribute!
        '''
        if not value:
            raise Exception('Article segment description is missing...')
        
        self._description = value

    @property
    def segment_order(self):
        return self._segment_order