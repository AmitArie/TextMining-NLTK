#/usr/bin/python3

import json
import pandas as pd
from nltk.tag import StanfordNERTagger
import nltk as nltk
import  concurrent.futures



st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

df = pd.read_csv('Full.csv', delimiter=',')

articles = [tuple(x) for x in df.values]

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
		print("article number: ", articleNUmber)
		article = {}
		article["name"] = articles[articleNUmber][ARTICLE_TITLE]
		article["sent_tag"] = tag_atricle_sentence(articles[articleNUmber][ARTICLE_BODY])
		json_data = json.dumps(article)
		return json_data


executor = concurrent.futures.ProcessPoolExecutor(10)
futures = [executor.submit(createFullTagOfArticle, i) for i in range(len(articles))]
concurrent.futures.wait(futures)


# with open("articles_tags_file.json", mode='w', encoding='utf-8') as f:
#     json.dump([], f)



# with open("articles_tags_file.json", mode='w', encoding='utf-8') as feedsjson:
# 	articles_list = []
	

# 	for i in range(0, 10):


# 		print(json_data)
# 	json.dump(articles_list, feedsjson)




