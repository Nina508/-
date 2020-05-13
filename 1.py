import json
import io
import csv

data = {}

with io.open("data.json", encoding='utf-8') as file:
    data = json.load(file)


def extract_first_features(dict):
    res = []
    for i in dict:
        for j in i.get('dialog'):
            res.append([i.get('dialog_id'), j.get('sender'), j.get('text')])
    return res


extract_first_features(data)

with io.open('data.csv', 'w', newline='', encoding='utf-8') as my_file:
    columns = ['dialog_id', 'sender_id', 'text']
    wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
    for i in extract_first_features(data):
        wr.writerow(i)
