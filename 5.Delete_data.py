# Delete Operation

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Test']
collections = db['Checkdata']

data = collections.delete_one({'salary' : '70000'})

print(data)

client.close()