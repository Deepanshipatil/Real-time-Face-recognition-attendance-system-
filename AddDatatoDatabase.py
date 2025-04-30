import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountsKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-2-29d01-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "salman":
        {
            "name": "Salman Khan",
            "major": "Movies",
            "starting_year": 2006,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "sharukh":
        {
            "name": "Sharukh Khan",
            "major": "Movies",
            "starting_year": 2006,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
        
}

for key, value in data.items():
    ref.child(key).set(value)