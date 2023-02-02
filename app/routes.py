from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "James",
        "last_name": "Grantham",
        "hobbies": "Skateboarding",
        "is_active": True
    }

    return me








#homework object oriented programming