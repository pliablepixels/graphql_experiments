from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaC: 
    def __init__(self):
        self.resolver = ObjectType('Query')
        self.resolver.set_field('getSchemaC', self.resolve_schemaC)
        logging.info('Schema C resolver is bound')

    def get_resolvers(self):
        return self.resolver

    def resolve_schemaC(self,obj,info):
        logging.info('Inside Schema C resolver')
        logging.info('None of schemaA or schemaB resolvers will be called after this')
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
        