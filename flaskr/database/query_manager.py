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
        *args: (db_model_object, db_table_name)
        '''
        query = None
        try:
            model_obj, table_name = self._parse_modify_table_args(args)
            
            insert_start_statement = f'INSERT INTO {table_name} (FIELDS_PLACEHOLDER) '
            insert_end_statement = 'VALUES (VALUES_PLACEHOLDER);'
            field_string = ''
            value_string = ''
            property_count = len(model_obj.__dict__.keys())
            for k, v in model_obj.__dict__.items():
                field_string += f'{k}'
                value_string += f'{v}'

                property_count -= 1
                if property_count > 0:
                    field_string += ', '
                    value_string += ', '
            
            query = insert_start_statement.replace('FIELDS_PLACEHOLDER', field_string) + insert_end_statement.replace('VALUES_PLACEHOLDER', value_string)
        except Exception as e:
            print(f"Couldn't build the insert query due to an error - {str(e)}")
        
        return query
    
    def make_update_query_by_id(self, *args, **kwargs):
        '''
        Builds a db update query with the relevant information included in the args/kwargs parameters.
        *args: (db_model_object, db_table_name)
        '''
        query = None
        try:
            model_obj, table_name = self._parse_modify_table_args(args)

            update_statement = f'UPDATE {table_name} SET VALUES_PLACEHOLDER WHERE id = {model_obj.id};'
            values_string = ''
            
            property_count = len(model_obj.__dict__.keys())
            for k, v in model_obj.__dict__.items():
                values_string += f'{k} = {v}'
                property_count -= 1
                if property_count > 0:
                    values_string += ', '
            
            query = update_statement.replace('VALUES_PLACEHOLDER', values_string)
        except Exception as e:
            print(f"Couldn't build the update query due to an error - {str(e)}")

        return query

    def make_remove_query(self, *args, **kwargs):
        '''
        Builds a db remove query with the relevant information included in the args/kwargs parameters.
        *args: ([where_clause_field_list], [where_clause_value_list], table_name)
        '''
        query = None
        try:
            where_clause_fields, where_clause_values, table_name = self._parse_modify_table_args(args)

            remove_statement = f'DELETE FROM {table_name} WHERE WHERE_CLAUSE_PLACEHOLDER;'
            where_clause_string = ''
            for i in range(len(where_clause_fields)):
                where_clause_string += f'{where_clause_fields[i]} = {where_clause_values[i]}'
                if i < len(where_clause_fields) - 1:
                    where_clause_string += ' AND '
            
            query = remove_statement.replace('WHERE_CLAUSE_PLACEHOLDER', where_clause_string)
        except Exception as e:
            print(f"Couldn't build the delete query due to an error - {str(e)}")

        return query
    
    def make_get_query(self, *args, **kwargs):
        '''
        Builds a db get query with the relevant information included in the args/kwargs parameters.
        *args: ([where_clause_field_list], [where_clause_value_list], table_name)
        '''
        query = None
        try:
            where_fields, where_values, table_name = self._parse_modify_table_args(args)

            get_statement = f'SELECT * FROM {table_name} WHERE WHERE_CLAUSE_PLACEHOLDER;'
            get_string = ''

            for i in range(len(where_fields)):
                get_string += f'{where_fields[i]} = {where_values[i]}'
                if i < len(where_fields) - 1:
                    get_string += ' AND '
            
            query = get_statement.replace('WHERE_CLAUSE_PLACEHOLDER', get_string)
        except Exception as e:
            print(f"Couldn't build the get query due to an error - {str(e)}")

        return query

    def _parse_modify_table_args(self, *args):
        if len(args) < 2:
            raise Exception('Arguments passed to a DB modify query are insuficient... Len of arguments passed is ', len(args))
        model_obj = args[0]
        table_name = args[1]

        return model_obj, table_name