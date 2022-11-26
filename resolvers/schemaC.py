from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaC: 
    def __init__(self):
        self.resolvers = []
        self.resolvers.append(ObjectType('Query'))
        self.resolvers[0].set_field('getSchemaC', self.resolve_query_getSchemaC)
        logging.info('Schema C Query resolver is bound')

    def get_resolvers(self):
        return self.resolvers

    def resolve_query_getSchemaC(self,obj,info):
        logging.info('Inside Schema C resolver')
        return {
                    'schemaA': {
                        'text_val': 'This is text inside SchemaC'
                    },
                    'schemaB': {
                        'text': 'This is text inside SchemaC',
                        'number':3

                    },
                    'moreData':3.333
                   
        }   
        