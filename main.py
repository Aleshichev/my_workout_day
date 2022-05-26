import requests
import os
from datetime import datetime

print(os.environ['MYAPP_ID'])

GENDER = "man"
WEIGHT_KG = 72
HEIGHT_CM = 182
AGE = 33
USERNAME = os.environ.get('MYUSERNAME')
USER_PASSWORD = os.environ.get('MYUSER_PASSWORD')

APP_ID = os.environ.get('MYAPP_ID')                         #"30a28927"
API_KEY = os.environ.get('MYAPI_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me wich exercises you did: ")
#POST request body:
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {

 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

sheet_endpoint = os.environ.get('MYSHEET_ENDPOINT')

today_date = datetime.now().strftime("%d%m%y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(
      USERNAME,
      USER_PASSWORD,
  ))
    print(sheet_response.text)


