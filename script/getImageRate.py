# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import collections

# 使用するタグデータを生成する
import getTagData

def getImageRate():
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    tagData = pd.read_csv("../data/getTagData.csv")

    imageRateAve = pd.Series([])
    i=0
    j=0
    while(j<len(data)):
        imageRate = 0
        for index, row in tagData.iterrows():
            if((str(row[0])) in str(data.iloc[j,6])):
                # タグ総数に占める割合の総和を求める
                imageRate = imageRate + row['タグに占める割合']

                # タグの個数
                i=str(data.iloc[j,6]).count(',')+1
        j = j + 1
        # 平均値を出す
        imageRateAve[j] = imageRate/i
    #print(imageRateAve)
    imageRateDF = pd.DataFrame(imageRateAve)
    imageRateDF.rename(columns={0 : 'imageRate'}, inplace=True)
    data = pd.concat([data, imageRateDF], axis=1).sort_values('imageRate', ascending=False)

    data.to_csv("../data/getImageRate.csv")
    print('Generate ../data/getImageRate.csv')
getImageRate()
