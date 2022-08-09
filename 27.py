""" Write a Python program to create Doctor collections under DbInfowith following fields
as Doctor table {Doctor_Id,Doctor_Name,Hospital_Id, Joining_Date,Speciality, Salary,
Experience}
Write a code to
1. Insert 5 records in collections.
2. Update Experience of Doctors
3. Search records after updation
4. Sort documents in ascending """

# list of dictionary of doctors with their speciality and salary
doctors_list = [
    {
        "doc_id": 1,
        "name": "Dr. John",
        "speciality": "Cardiology",
        "salary": 60000,
        "h_id": 1,
        "joined": "11/11/2000",
        "experience": 20
    },
    {
        "doc_id": 2,
        "name": "Dr. Paul",
        "speciality": "Orthopedics",
        "salary": 50000,
        "h_id": 1,
        "joined": "25/09/2019",
        "experience": 3
    },
    {
        "doc_id": 3,
        "name": "Dr. Smith",
        "speciality": "Cardiology",
        "salary": 70000,
        "h_id": 2,
        "joined": "25/11/2017",
        "experience": 5
    },
    {
        "doc_id": 4,
        "name": "Dr. Peter",
        "speciality": "Orthopedics",
        "salary": 80000,
        "h_id": 1,
        "joined": "09/04/2006",
        "experience": 10,
    },
    {
        "doc_id": 5,
        "name": "Dr. James",
        "speciality": "Cardiology",
        "salary": 90000,
        "h_id": 3,
        "joined": "10/10/2000",
        "experience": 15
    }
]


def get_db():
    from pymongo import MongoClient
    # load the MongoDB URI from the environment variable
    from dotenv import load_dotenv
    import os
    load_dotenv()

    client = MongoClient(os.getenv('MONGODB_URI'))
    # client = MongoClient('mongodb://localhost:27017')
    db = client.DbInfo

    return db


db = get_db()

db.drop_collection("doctors")

col_doctors = db.doctors
col_doctors.insert_many(doctors_list)


def print_doctors(results):
    print("-" * 50)
    print(f"{'Name':<20} {'Speciality':<20} {'Salary':<20}")
    print("-" * 50)
    for result in results:
        print(
            f"{result['name']:<20} {result['speciality']:<20} {result['salary']:<20}")
    print()


def update_experience(results):
    for result in results:
        result['experience'] = result['experience'] + 1
        col_doctors.update_one(
            {'doc_id': result['doc_id']},
            {'$set': result}
        )
    print("Updated successfully")


def search_by_id(id):
    result = col_doctors.find_one({'doc_id': id})
    print("-" * 50)
    print(f"{'Name':<20} {'Speciality':<20} {'Salary':<20}")
    print("-" * 50)
    print(
        f"{result['name']:<20} {result['speciality']:<20} {result['salary']:<20}")


def sorted_by_salary():
    results = col_doctors.find().sort('salary', 1)
    print_doctors(results)


sorted_by_salary()
search_by_id(1)
