""" Javascript Object Notation"""
import json

# people_string = """
# {
#     "people": [
#         {
#             "name":"John Smith",
#             "phone":"615-555-7164",
#             "emails":["johnsmith@bogusemail.com", "john.smith@work-place.com"],
#             "has-license":false
#         },
#         {
#             "name":"Jane Doe",
#             "phone":"560-555-5153",
#             "emails":null,
#             "has-license":true
#         }
#     ]
# }
# """
# data = json.loads(people_string)

# for person in data["people"]:
#     del person["phone"]

# new_string = json.dumps(data, indent=3)
# print(new_string)

with open("states.json") as f:
    data = json.load(f)

for state in data["states"]:
    del state["area_codes"]

with open("new_states.json", "w") as f:
    json.dump(data, f, indent=3)
