from dotenv import load_dotenv
import os
import requests
from datetime import datetime
load_dotenv()

app_id = os.getenv("app_id")
app_key = os.getenv("app_key")
auth = os.getenv("auth")

headers = {
    "x-app-id":app_id,
    "x-app-key":app_key
}

user_input = input("which exercises did you do? ")
exercise_body = {
    "query":user_input,
    "weight_kg": 80,
    "height_cm": 180,
    "age": 20
}



host_domain = "https://trackapi.nutritionix.com"
exercises_endpoint = "/v2/natural/exercise"
exercises_url = f"{host_domain}{exercises_endpoint}"

sheety_url = "https://api.sheety.co/23007e722a0baba09c86900023f703e6/workout/exercise"

exercise_response = requests.post(url=exercises_url,json=exercise_body,headers=headers)
exercise_data = exercise_response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_data["exercises"]:
    sheety_body = {
        "exercise": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

header = {
    "Authorization" : auth
}

sheety_response = requests.post(url=sheety_url,json=sheety_body, headers=header)
sheety_response.raise_for_status()