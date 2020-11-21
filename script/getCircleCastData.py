# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import collections

def getCircleData():
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    data['date'] = pd.to_datetime(data['date'])
    
    # サークル情報のパス
    circle_path = '../data/getCircleData.csv'
    # 声優情報のパス
    cast_path = '../data/getCastData.csv'
    
    # サークルの情報をCSVに出力する
    print("Generate " + circle_path)
    circle_data = pd.Series(data['circle'].value_counts())
    circle_data = pd.concat([circle_data, circle_data/len(data)], axis=1)
    circle_data.columns = ['出現数','出現率']
    circle_data.to_csv(circle_path, header=True)
    
    # ここから出演声優情報の処理
    # 調査対象の声優名をデータから排除する
    exc_cast = ""
    
    #data = data[(data['date']>=dt.datetime(2019,1,1)) & (data['date']<=dt.datetime(2019,12,31))]
    spl_cast = data['cast'].str.split(',', expand=True)
    
    castData = None
    for clnm in spl_cast:
        spl_cast.loc[spl_cast[clnm] == '-', clnm] = None
        spl_cast.loc[spl_cast[clnm] == exc_cast, clnm] = None
        castData = pd.concat([castData, spl_cast[clnm]])
    
    info = castData.value_counts()
    info = pd.concat([info, info/len(data)], axis=1)
    info.columns = ['出現数','出現率']
    print("Generate " + cast_path)
    info.to_csv(cast_path, header=True)

getCircleData()
