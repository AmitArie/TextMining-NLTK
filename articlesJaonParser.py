import json

with open('articles_tags_file.json') as data_file:    
    data = json.load(data_file)
    for entry in data:
    	print(json.loads(entry)["tag"])