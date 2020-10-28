# _*_ coding: utf-8 _*_

import pandas as pd
import datetime as dt

def getDescribe():
    # データの読み込み
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    data['date'] = pd.to_datetime(data['date'])

    # このスクリプトは要約統計量を得るためのものです．
    with open('../log/getDescribe.txt', mode='w') as f:
        f.write(str(data.describe()))
    print("Generate ../log/getDescribe.txt")

getDescribe()
