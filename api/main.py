from flask import Flask, json
from flask_cors import CORS, cross_origin

physicians = [
    {   
        "id": 1,
        "name": "Julius Hibbert",
        "email": "hibbert@notablehealth.com",
        "appointments": [
            {
                "id": 1,
                "name": "Sterling Archer",
                "time": "8:00AM",
                "kind": "New Patient"
            },
            {
                "id": 2,
                "name": "Cyril Figis",
                "time": "8:30AM",
                "kind": "Follow-up"
            },
            {
                "id": 3,
                "name": "Ray Gilette",
                "time": "9:00AM",
                "kind": "Follow-up"
            },
            {
                "id": 4,
                "name": "Lana Kane",
                "time": "9:30AM",
                "kind": "New Patient"
            },
            {
                "id": 5,
                "name": "Pam Poovey",
                "time": "10:00AM",
                "kind": "New Patient"
            },

        ]
    },
    { 
        "id": 2,
        "name": "Algernop Krieger", 
        "email": "krieger@notablehealth.com",
        "appointments": [
            {
                "id": 1,
                "name": "Sterling Archer 2",
                "time": "8:00AM",
                "kind": "New Patient"
            },
            {
                "id": 2,
                "name": "Cyril Figis 2",
                "time": "8:30AM",
                "kind": "Follow-up"
            },
            {
                "id": 3,
                "name": "Ray Gilette 2",
                "time": "9:00AM",
                "kind": "Follow-up"
            },
            {
                "id": 4,
                "name": "Lana Kane 2",
                "time": "9:30AM",
                "kind": "New Patient"
            },
            {
                "id": 5,
                "name": "Pam Poovey 2",
                "time": "10:00AM",
                "kind": "New Patient"
            },

        ]
    },
    { 
        "id": 3,
        "name": "Nick Rivera", 
        "email": "rivera@notablehealth.com",
        "appointments": [
            {   "id": 1, 
                "name": "Sterling Archer 3",
                "time": "8:00AM",
                "kind": "New Patient"
            },
            {
                "id": 2,
                "name": "Cyril Figis 3",
                "time": "8:30AM",
                "kind": "Follow-up"
            },
            {
                "id": 3,
                "name": "Ray Gilette 3",
                "time": "9:00AM",
                "kind": "Follow-up"
            },
            {
                "id": 4,
                "name": "Lana Kane 3",
                "time": "9:30AM",
                "kind": "New Patient"
            },
            {
                "id": 5,
                "name": "Pam Poovey 3",
                "time": "10:00AM",
                "kind": "New Patient"
            },

        ]
    },
]

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

@api.route('/physicians', methods=['GET'])
@cross_origin()

def get_physicians():
    return json.dumps(physicians)

if __name__ == "__main__":
    api.run()