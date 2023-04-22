import json
with open("responses/company1.json", "r") as json_handle:
    pre_dict = json.load(json_handle)

from pprint import pprint
pprint(pre_dict)