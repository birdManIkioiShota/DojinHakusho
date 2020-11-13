# _*_ coding: utf-8 _*_

from io import StringIO
import pandas as pd

import MeCab

m = MeCab.Tagger()

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

words = None
for index, row in data.iterrows():
    analyzed = m.parse(row['title'])
    df_analyzed = pd.read_csv(StringIO(analyzed), delimiter='\t',names=['1','2','3','4','5','6','7','8'])
    
        
    words = pd.concat([words, df_analyzed])

#print(words['1'].value_counts())

words = words[words['5'].str.contains("名詞", na=False)]
words = words.reset_index()
print(words['1'].value_counts())
words = words['1'].value_counts()/len(data)
words.to_csv("../data/noun.csv")
