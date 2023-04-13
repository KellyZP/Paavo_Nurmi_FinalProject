#functions.py

import json

def read_JSON():
    with open('EncryptedGroupHints Spring 2023 Section 001.json', 'r') as f:
        temp = f.read()
    data = json.loads(temp)
    values = [value for key, value in data.items()]
    print(values)



def load_file(file_path):
    try:
        tmp_lines = [line.strip().lower() for line in open(file_patj)]
    except:
        tmp_lines = None
    return tmp_lines
    