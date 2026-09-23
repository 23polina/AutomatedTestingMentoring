import json
import os
from datetime import date

def load_people_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File NOT found {file_path}")
    else:
        with open(file_path) as data:
            return json.load(data)

def filter_people_under18():
    people_data = load_people_from_file("json_program1.json")
    today = date.today()
    final_result = []
    for people in people_data:
        transformed_date = date.fromisoformat(people["birth_date"])
        if transformed_date > date(today.year - 18, today.month, today.day):
            final_result.append(people)
    return final_result
