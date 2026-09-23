import json
from datetime import date


def filter_people_under18():
    with open("json_program1.json") as people_data:
        unpacked_data = json.load(people_data)
    today_date = date.today()
    final_result = []
    for people in unpacked_data:
        transformed_date = date.fromisoformat(people["birth_date"])
        if transformed_date > date(today_date.year - 18, today_date.month, today_date.day):
            final_result.append(people)
    return final_result
