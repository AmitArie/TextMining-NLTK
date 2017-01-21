#/usr/bin/python3

import pandas as pd
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('Full.csv', delimiter=',')

# Or export it in many ways, e.g. a list of tuples
articles = [tuple(x) for x in df.values]

# or export it as a list of dicts


ARTICLE_ID = 2
ARTICLE_SOURCE = 3
ARTICLE_DATE = 4
ARTICLE_TITLE = 5
ARTICLE_BODY = 6


for i in range(10):
	print(st.tag(articles[i][ARTICLE_BODY].split()))

