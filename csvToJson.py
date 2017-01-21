#/usr/bin/python3

import json
import pandas as pd
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

df = pd.read_csv('Full.csv', delimiter=',')

articles = [tuple(x) for x in df.values]

ARTICLE_ID = 2
ARTICLE_SOURCE = 3
ARTICLE_DATE = 4
ARTICLE_TITLE = 5
ARTICLE_BODY = 6

with open("articles_tags_file.json", mode='w', encoding='utf-8') as f:
    json.dump([], f)


with open("articles_tags_file.json", mode='w', encoding='utf-8') as feedsjson:
	articles_list = []
	for i in range(len(articles)):
		print("article number: ", i)
		article = {}
		article["name"] = articles[i][ARTICLE_TITLE]
		article["tag"] = st.tag(articles[i][ARTICLE_BODY].split())
		json_data = json.dumps(article)
		articles_list.append(json_data)
		
	json.dump(articles_list, feedsjson)



