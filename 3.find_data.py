# Create a Connections

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# print(client)

# Create a DB

db = client['Test']
collections = db['Checkdata']

# Find Data

one = collections.find({'name' : 'Umang'})

for item in one:
    print(one)

client.close()
