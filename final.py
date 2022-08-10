import json
import os
import requests
import sys

BASE_URL = sys.argv[1]

# BASE_URL = "https://2d426e44-0b78-4936-a179-02556024fdbe.mock.pstmn.io"

PATH1 = "/forms/elements"
PATH2 = "/forms"
DIR_PATH = "data/"

X = "data"
sub_file = [DIR_PATH + file for file in os.listdir(X)]

for dir in sub_file:
    print(dir)
    for i in os.listdir(dir + "/"):
        path = os.path.join(dir, i)
        with open(path, 'r') as f:
            json_obj = json.load(f)
            if "data/forms" in path:
                r = requests.post(BASE_URL + PATH2, data=json_obj)
            if "data/elements" in path:
                r = requests.post(BASE_URL + PATH1, data=json_obj)
            if r.status_code != 200:
                print(r, "error")
                print(path)
            else:
                print(r, "success")
                print(path)