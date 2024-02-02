# Creating a Database with Python MongoDB

from pymongo import MongoClient

# if __name__ == "__main__":
try:
    print("Welcome, To Python MongoDB")

    client = MongoClient("mongodb://localhost:27017/")
    print(client)


except Exception as e:
    print("Exception Error")
