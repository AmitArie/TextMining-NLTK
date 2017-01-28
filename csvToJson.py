#/usr/bin/python3

import json
import pandas as pd
from nltk.tag import StanfordNERTagger
import nltk as nltk
import  concurrent.futures



st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

df = pd.read_csv('Full.csv', delimiter=',')

articles = [tuple(x) for x in df.values]
articles_list = []

ARTICLE_ID = 2
ARTICLE_SOURCE = 3
ARTICLE_DATE = 4
ARTICLE_TITLE = 5
ARTICLE_BODY = 6

def tag_atricle_sentence(article):
	sent_tags = {}
	sent  = nltk.sent_tokenize(article)

	for i in range(len(sent)):
		sent_tags[str(i)] = []
		sent_tags[str(i)] = st.tag(sent[i].split())

	return sent_tags


def createFullTagOfArticle(articleNUmber):
	file_name = str(articleNUmber) + ".json"
	with open(file_name, mode='w', encoding='utf-8') as f:
		print("article number: ", articleNUmber)
		article = {}
		article["name"] = articles[articleNUmber][ARTICLE_TITLE]
		article["sent_tag"] = tag_atricle_sentence(articles[articleNUmber][ARTICLE_BODY])
		json_data = json.dumps(article)
		print("article number   ", articleNUmber, "Has finished")
		json.dump(json_data, f)

for i in range((len(articles))):
	createFullTagOfArticle(i);




