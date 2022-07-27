import json
import os
import requests

BASE_URL = input("Enter your BASE URL: ")

# BASE_URL = "https://2d426e44-0b78-4936-a179-02556024fdbe.mock.pstmn.io"

PATH = "/forms/elements"
DIR_PATH = "data/"

files = []
X = "data"
sub_file = [DIR_PATH + file for file in os.listdir(X)]

for f in sub_file:
    for i in os.listdir(f + "/"):
        file_path = (f + "/" + i)
        files.append(file_path)

for path in files:
    with open(path, 'r') as f:
        json_obj = json.load(f)
        r = requests.post(BASE_URL+PATH, data=json_obj)
        if r.status_code != 200:
            print(r, "error")
            print(path)
        else:
            print(r, "success")
            print(path)
