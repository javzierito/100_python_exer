import json
with open("responses/company1.json", "r+") as json_handle:
    pre_dict = json.load(json_handle)
    pre_dict["employees"].append({'firstName': 'Albert', 'lastName': 'Bert'})
    json_handle.seek(0)
    json.dump(pre_dict, json_handle, indent=4, sort_keys=True)
    json_handle.truncate()