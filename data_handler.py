import os
import json

DATA_FILE = "data.json"

DEFAULT_DATA = {
    "balance": 0,
    "last_daily": None,
    "daily_streak": 0,
    "bio": None
}

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user(user_id):
    """Get user data or create one if new"""
    data = load_data()
    uid = str(user_id)
    if uid not in data:
        data[uid] = DEFAULT_DATA.copy()
        save_data(data)
    return data[uid]

def save_user(user_id, user_data):
    """Updates specific field of user data"""
    data = load_data()
    uid = str(user_id)
    data[uid] = user_data
    save_data(data)
