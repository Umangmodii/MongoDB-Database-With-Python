from pymongo import MongoClient

# if __name__ == "__main__":
print("Welcome, To Python MongoDB")

client = MongoClient("mongodb://localhost:27017/")
print(client)

# Create a new DB
db = client['Test']

# Create a new Collection Name
collections = db['Checkdata']

# Single Data insert in MongoDB
dictionary = {'name': 'Umang', 'Age': 21}
collections.insert_one(dictionary)

# Multiple Data insert in MongoDB

data = [
    {
        'name': 'Parth',
        'Age': 20,
        'Salary': 30000
    },

    {
        'name': 'Raj',
        'Age': 30,
        'Salary': 50000
    },
]

collections.insert_many(data)

client.close()