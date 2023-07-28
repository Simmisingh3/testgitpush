from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://simmisingh22299:8QCcFZOmyRzXDHXe@cluster0.mwtduly.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
    "name":"simmi",
    "email":"simmi@ineuron.ai",
    "surname":"singh"
}
db=client['mondotest']
coll = db['test1']
coll.insert_one(d )
print(d)