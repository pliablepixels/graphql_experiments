from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
import logging
logging.basicConfig(level=logging.INFO)

from resolvers.schemaA import SchemaA
from resolvers.schemaB import SchemaB
from resolvers.schemaC import SchemaC

list_of_resolvers = [SchemaA(), SchemaB(), SchemaC()]
types_list = load_schema_from_path('./schemas/')
resolver_list = []

for item in list_of_resolvers:
    resolvers = item.get_resolvers()
    for i in resolvers:
        resolver_list.append(i)
    schema = make_executable_schema(types_list , resolver_list)
    app = GraphQL(schema, debug=True)