from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaB: 
    def __init__(self):
        self.resolvers = []
        self.resolvers.append(ObjectType('Query'))
        self.resolvers[0].set_field('getSchemaB', self.resolve_query_getSchemaB)
        logging.info('Schema B query resolver is bound')

    def get_resolvers(self):
        return self.resolvers

    def resolve_query_getSchemaB(self,obj,info):
        logging.info('Inside Schema B resolver')
        return {
                    'text':'This is SchemaB text from resolver',
                    'number':42
        }   
        