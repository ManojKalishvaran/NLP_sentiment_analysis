import nltk
import re
nltk.download('all')

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
df=pd.read_csv('review.csv')
#print(df)
senti=[]
for row in df['Review']:
  blb=TextBlob(row)
  sentiment=blb.sentiment.polarity
  if sentiment<-0.1:
    sentiy='negative'
  elif sentiment>0.1:
    sentiy='positive'
  else:
    sentiy='neutral'
  senti.append(sentiy)
print(senti)
sns.countplot(x=senti)
plt.show()