import uuid

class User:
    '''
    This class is a holder for a single users's attributes.
    '''

    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id', str(uuid.uuid4()))
        self._full_name = kwargs.get('full_name', '')
        self._set_user_name(kwargs.get('user_name', None))
        self._email = kwargs.get('email', '')
        self._set_password(kwargs.get('password', None))
        self._type = kwargs.get('type', 'regular') # Users can be regular or admin

    @property
    def id(self):
        return self._id

    @property
    def full_name(self):
        return self._full_name
    
    @property
    def user_name(self):
        return self._full_name
    
    def _set_user_name(self, value):
        '''
        Set username only upon initialization. It is a required attribute!
        '''
        if not value:
            raise Exception('User name must be set...')
        
        self._user_name = value

    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    
    def _set_password(self, value):
        '''
        Set password only upon initialization. It is required!
        '''
        if not value:
            raise Exception('Password must be set...')
        
    @property
    def type(self):
        return self._type