import json
import os
import requests

ENDPOINT = "https://3dd0b4e6-d245-4435-83a2-cc3cf5778593.mock.pstmn.io/forms/element"


DIR_PATH = "data/elements/"

# list of paths of all the json files in the directory
files = [DIR_PATH + file for file in os.listdir(DIR_PATH)]

for path in files:
    with open(path, 'r') as f:
        json_obj = json.load(f)
        r = requests.post(ENDPOINT, data=json_obj)
        print(r)
        print(path)

