""" Write a python code to create a NOSQL(MongoDb) database DbInfo and use this
database object to create collection customer and write code for
1. Insert 10 records (Use Dictionary) with fields (Name, Cust_ID, DOJ, Address,
E-mail, Mobile Number, Experience)
2. Select all records from the collection
3. Search records by specific names
4. Delete records by specific Cust_ID """

customers = [{"cust_id": 1, "name": "Jada Moult", "address": "992 Grim Drive", "DOJ": "9/24/2005", "email": "jmoult0@t-online.de", "mobile_no": "5418959207", "experience": 24},
             {"cust_id": 2, "name": "Amandie Larner", "address": "9 Melvin Street", "DOJ": "8/24/2003",
              "email": "alarner1@msu.edu", "mobile_no": "1712479832", "experience": 14},
             {"cust_id": 3, "name": "Estevan Reason", "address": "37 Mallory Court", "DOJ": "9/25/2014",
              "email": "ereason2@ow.ly", "mobile_no": "1106160594", "experience": 29},
             {"cust_id": 4, "name": "Wayne Rohan", "address": "6 Novick Road", "DOJ": "10/3/2010",
              "email": "wrohan3@vkontakte.ru", "mobile_no": "4644078677", "experience": 30},
             {"cust_id": 5, "name": "Laurette De Hailes", "address": "13 Sunbrook Center", "DOJ": "1/30/2020",
              "email": "lde4@hugedomains.com", "mobile_no": "7664607423", "experience": 33},
             {"cust_id": 6, "name": "Titos Olding", "address": "13156 Nevada Way", "DOJ": "12/20/2017",
              "email": "tolding5@amazon.co.jp", "mobile_no": "9441877520", "experience": 17},
             {"cust_id": 8, "name": "Zackariah Pawels", "address": "001 Elgar Park", "DOJ": "1/23/2007",
              "email": "zpawels7@alibaba.com", "mobile_no": "8504165686", "experience": 34},
             {"cust_id": 9, "name": "Larissa Leppard", "address": "903 Carey Street", "DOJ": "3/22/2013",
              "email": "lleppard8@ucsd.edu", "mobile_no": "2555198862", "experience": 27},
             {"cust_id": 10, "name": "Corabelle Teideman", "address": "2 Almo Way", "DOJ": "6/1/2004", "email": "cteideman9@nydailynews.com", "mobile_no": "7667863346", "experience": 11}]


def get_db():
    from pymongo import MongoClient
    # get mongodb connection string from environment variable
    from dotenv import load_dotenv
    import os
    
    load_dotenv()

    client = MongoClient(os.getenv("MONGODB_URI"))
    # client = MongoClient("mongodb://localhost:27017")
    db = client.test

    return db


db = get_db()

db.drop_collection("customers")
cust = db.customers

cust.insert_many(customers)


def print_result(results):
    print("-" * 90)
    print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Mobile No':<12} {'Exp':^5} {'Address':<10}")
    print("-" * 90)
    for result in results:
        print(f"{result['cust_id']:<5} {result['name']:<20} {result['email']:<25} {result['mobile_no']:<12} {result['experience']:^5} {result['address']:<10}")
    print()


def get_all_customers():
    results = cust.find()
    print_result(results)


def search_customer(name):
    results = cust.find({"name": name})
    print_result(results)


def delete_customer(cust_id):
    cust.delete_one({"cust_id": cust_id})
    print(f"Customer with ID {cust_id} deleted successfully")
    print()


# get_all_customers()
search_customer("Jada Moult")
delete_customer(10)
get_all_customers()
