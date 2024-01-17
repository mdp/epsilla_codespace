from pyepsilla import vectordb

client = vectordb.Client(host='localhost', port='8888')
client.load_db(db_name="MyDB", db_path="/data/epsilla")
client.use_db(db_name="MyDB")

client.create_table(
    table_name="MyTable",
    table_fields=[
        {"name": "ID", "dataType": "INT", "primaryKey": True},
        {"name": "Doc", "dataType": "STRING"},
    ],
    indices=[
      {"name": "Index", "field": "Doc"},
    ]
)

client.insert(
    table_name="MyTable",
    records=[
        {"ID": 1, "Doc": "Jupiter is the largest planet in our solar system."},
        {"ID": 2, "Doc": "Cheetahs are the fastest land animals, reaching speeds over 60 mph."},
        {"ID": 3, "Doc": "Vincent van Gogh painted the famous work \"Starry Night.\""},
        {"ID": 4, "Doc": "The Amazon River is the longest river in the world."},
        {"ID": 5, "Doc": "The Moon completes one orbit around Earth every 27 days."},
    ],
)

client.query(
    table_name="MyTable",
    query_text="Celestial bodies and their characteristics",
    limit=2
)

# Result
# {
#     'message': 'Query search successfully.',
#     'result': [
#         {'Doc': 'Jupiter is the largest planet in our solar system.', 'ID': 1},
#         {'Doc': 'The Moon completes one orbit around Earth every 27 days.', 'ID': 5}
#     ],
#     'statusCode': 200
# }