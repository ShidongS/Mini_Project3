from pymongo import MongoClient
from bson.son import SON
import pprint
client = MongoClient()
db = client.Mini3
pictures=db.pictures
# Credit to http://api.mongodb.com/python/current/examples/aggregation.html
while(1):
    a=input("Please select your function: 1.Show account of most pictures; 2.Show most popular tags; 3.Search\n")
    if a=="1":
        pipeline = [
        {"$unwind": "$account_name"},
        {"$group": {"_id": "$account_name", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("_id", -1)])}
        ]
        pprint.pprint(list(pictures.aggregate(pipeline)))
        print("\n")

    if a=='2':
        pipeline = [
         {"$unwind": "$tags"},
         {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
         {"$sort": SON([("count", -1), ("_id", -1)])}
         ]
        pprint.pprint(list(pictures.aggregate(pipeline)))
        print("\n")

    if a=='3':
	    b=input("Please type in the tag you wang to search:")
	    k=[]
	    for x in pictures.find({"tags":b},{"account_name":1,"_id":0}):
	        k.append(x["account_name"])
	    k=list(set(k))
	    if len(k)==0:
	    	print("No account has this tag")
	    else:
	        print("The following account(s) have this tag: ")
	        print(k)
	    print("\n")

    if a!='1' and a!='2' and a!='3':
    	print("Please select the right function\n")



