import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Test']
collections = db['Checkdata']

showdata = client.list_database_names()
print(showdata)


client.close()