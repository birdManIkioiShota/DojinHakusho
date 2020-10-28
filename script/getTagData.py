# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import collections

def getTagData():
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    data['date'] = pd.to_datetime(data['date'])
    
    spl_tag = data['tag'].str.split(',', expand=True)
    
    # タグの出現数と出現率をカウントします
    tagData = None
    for clnm in spl_tag:
        # 性癖と関係なさそうなタグを排除しています
        # 適当に編集してください
        spl_tag.loc[spl_tag[clnm] == 'ASMR', clnm] = None
        spl_tag.loc[spl_tag[clnm] == 'バイノーラル/ダミヘ', clnm] = None
        spl_tag.loc[spl_tag[clnm] == '萌え', clnm] = None
        
        tagData = pd.concat([tagData, spl_tag[clnm]])
        
    info = pd.Series(tagData.value_counts())
    pd.set_option('display.max_rows', len(info))

    info = pd.concat([info, info/len(info)], axis=1)
    tagSum = info.iloc[:,0].sum()
    info = pd.concat([info, info.iloc[:,0]/tagSum], axis=1)
    info.columns = ['出現数','出現率','タグに占める割合']
    
    path = '../data/getTagData.csv'
    print('Generate ' + path)
    info.to_csv(path)

getTagData()
