class QueryManager:
    '''
    This class is responsible for providing the relevant queries for db operations. Main db operations:
        - add table entry
        - update table entry
        - remove table entry
        - get table entry
    '''

    def __init__(self):
        '''
        Empty constructor as no attributes are required for the manager to work.
        '''
        pass

    def make_insert_query(self, *args, **kwargs):
        '''
        Builds a db insert query with the relevant information included in the args parameter.
        *args includes 2 lists - the first one is with all fields in order and the second one includes the relevant values for each one respectively. The last item in the args parameter is the name of the table we will insert into.
        '''
        query = None
        try:
            fields = args[0]
            values = args[1]
            table_name = args[2]

            if len(fields) != len(values):
                raise Exception('Fields and values parameters do not match...')
            
            insert_start_statement = f'INSERT INTO {table_name} (FIELDS_PLACEHOLDER) '
            insert_end_statement = 'VALUES (VALUES_PLACEHOLDER);'
            field_string = ''
            value_string = ''
            for i in range(len(fields)):
                field_string += fields[i]
                value_string += values[i]
            
            query = insert_start_statement.replace('FIELDS_PLACEHOLDER', field_string) + insert_end_statement.replace('VALUES_PLACEHOLDER', value_string)
        except Exception as e:
            print(f"Couldn't build the insert query due to an error - {str(e)}")
        
        return query


    def make_update_query(self, *args, **kwargs):
        '''
        Builds a db update query.
        '''

    def make_remove_query(self, *args, **kwargs):
        '''
        Builds a db remove query.
        '''
    
    def make_get_query(self, *args, **kwargs):
        '''
        Builds a db get query.
        '''