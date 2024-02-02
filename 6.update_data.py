
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Test']
collections = db['Checkdata']

prev = {'name' : 'Raj'}
next = {'$set' : {'Salary' : '70000'}}
data = collections.update_one(prev,next)
data = (data.modified_count)

client.close()
