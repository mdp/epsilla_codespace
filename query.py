from pprint import pprint
from pyepsilla import vectordb

client = vectordb.Client(host='localhost', port='8888')
client.load_db(db_name="MyDB", db_path="/data/epsilla")
client.use_db(db_name="MyDB")

result = client.query(
    table_name="MyTable",
    query_text="Celestial bodies and their characteristics",
    limit=2
)

pprint(result)

# Result
# {
#     'message': 'Query search successfully.',
#     'result': [
#         {'Doc': 'Jupiter is the largest planet in our solar system.', 'ID': 1},
#         {'Doc': 'The Moon completes one orbit around Earth every 27 days.', 'ID': 5}
#     ],
#     'statusCode': 200
# }