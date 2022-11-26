from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaB: 
    def __init__(self):
        self.resolver = ObjectType('Query')
        self.resolver.set_field('getSchemaB', self.resolve_schemaB)
        logging.info('Schema B resolver is bound')

    def get_resolvers(self):
        return self.resolver

    def resolve_schemaB(self,obj,info):
        logging.info('Inside Schema B resolver')
        return {
                    'text':'This is SchemaB text from resolver',
                    'number':42
        }   
        