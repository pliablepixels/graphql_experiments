from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaA: 
    def __init__(self):
        self.resolver = ObjectType('Query')
        self.resolver.set_field('getSchemaA', self.resolve_schemaA)
        logging.info('Schema A resolver is bound')

    def get_resolvers(self):
        return self.resolver

    def resolve_schemaA(self,obj,info):
        logging.info('Inside Schema A resolver')
        return {
                    'text_val':'This is SchemaA text from resolver'
        }   
        