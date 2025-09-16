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
            fields, values, table_name = self._parse_modify_table_args(args)
            
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
        Builds a db update query with the relevant information included in the args/kwargs parameters.
        *args: ([field_list], [value_list], table_name, [where_clause_fields], [where_clause_values])
        '''
        query = None
        try:
            fields, values, table_name = self._parse_modify_table_args(args)

            where_fields = args[3]
            where_values = args[4]
            if len(where_fields) != len(where_values):
                raise Exception('Fields and values parameters for the WHERE clause do not match...')

            update_statement = f'UPDATE {table_name} SET VALUES_PLACEHOLDER WHERE WHERE_CLAUSE_PLACEHOLDER;'
            values_string = ''
            where_clause_string = ''

            for i in range(len(fields)):
                values_string += f'{fields[i]} = {values[i]}'
                if i < len(fields) - 1:
                    values_string += ', '
            
            for i in range(len(where_fields)):
                where_clause_string += f'{where_fields[i]}={where_values[i]}'
                if i < len(where_fields):
                    where_clause_string += ' AND '
            
            query = update_statement.replace('VALUES_PLACEHOLDER', values_string).replace('WHERE_CLAUSE_PLACEHOLDER', where_clause_string)
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
        Builds a db get query.
        '''

    def _parse_modify_table_args(self, *args):
        fields = args[0]
        values = args[1]
        table_name = args[2]

        if len(fields) != len(values):
            raise Exception('Fields and values parameters do not match...')
        elif len(fields) == 0:
            pass # TODO implement logic when the fields/values lists are empty

        return fields, values, table_name