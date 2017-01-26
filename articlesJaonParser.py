#!/usr/bin/python3

import json
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')


TAG_TYPE = 1

def get_companies_from_tags(tags):
	companies = []
	for tag in tags:
		if tag[TAG_TYPE] == "ORGANIZATION":
			companies.append(tag)
	return companies



def get_companies_from_article (article):
	companies = {}
	companies["title_companies"] = get_companies_from_tags(st.tag(article["name"].split()))
	companies["body_companies"] = get_companies_from_tags(article["tag"])

	return companies


with open('articles_tags_file.json') as data_file:    
    data = json.load(data_file)
    # for article_number in range(len(data)):
    for article_number in range(1):
    	article_json = json.loads(data[article_number])
    	print(get_companies_from_article(article_json))








