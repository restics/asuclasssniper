import pingme
import json
import SMS
import re

with open('usernames.json') as json_file:
    db = json.load(json_file)
    for email in db.keys():
        message = ""
        for code in db.get(email):
            message += (pingme.look_up_course_by_id(code,email))
        if re.search(r'(.)', message) != None:
            print(f'Sending email to {email}')
            SMS.send(message, email)
