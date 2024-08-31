import os
import PyMongo
if os.path.exists("env.py"):
    import evn


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "recipe_book"
COLLECTION = "user"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: 5s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

for doc in documents:
    print(doc)