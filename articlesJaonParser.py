#!/usr/bin/python3

import json
from nltk.tag import StanfordNERTagger
import collections

i = 0
for article_number in range(1):
	file_name = str(article_number) + ".json"
	with open(file_name) as json_article:    
		article = json.loads(json.load(json_article))
		# print(data["sent_tag"])

		print("Article name: ", article["name"])
		print("Article number: ", i)
		sent = [ [int(k),v] for k, v in article["sent_tag"].items() ]
		sent.sort(key=lambda x: x[0])

		for s in sent:
			print(s[1])
			print("  ")
	i += 1







