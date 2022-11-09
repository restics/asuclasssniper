import pingme
import json


with open('usernames.json') as json_file:
    db = json.load(json_file)
    print(db)

    for email in db.keys():
        for code in db.get(email):
            pingme.look_up_course_by_id(code,email)