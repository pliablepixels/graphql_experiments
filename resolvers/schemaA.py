from ariadne import ObjectType
import logging
logging.basicConfig(level=logging.INFO)

class SchemaA: 
    def __init__(self):
        self.resolvers = []
        self.resolvers.append(ObjectType('Query'))
        self.resolvers[0].set_field('getSchemaA', self.resolve_query_getSchemaA)
        self.resolvers.append(ObjectType('SchemaA'))
        #self.resolvers[1].set_type_resolver(self.resolve_type_schemaA)
        self.resolvers[1].set_field('text_val', self.resolve_type_schemaA)
        logging.info('Schema A resolver is bound')

    def get_resolvers(self):
        return self.resolvers

    def resolve_query_getSchemaA(self,obj,info):
        logging.info('Inside Schema A QUERY resolver')
        return {
                    'text_val':'This is SchemaA text from resolver'
        }   
        
    def resolve_type_schemaA(self,obj,info):
        logging.info('Inside Schema A TYPE resolver')
        logging.info (f'obj:{obj}, info:{info}')
        return 'This is SchemaA text from resolver'
          
        