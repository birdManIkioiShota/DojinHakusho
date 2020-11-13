# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import datetime as dt
import collections

def getPriceSalesPlot():
    plt.figure()
    data = pd.read_csv("../data/getImageRate.csv")
    data['date'] = pd.to_datetime(data['date'])
    
    #data = data[data['sales'] < 2000]
    #print(data)
    # 売上と値段の関係をプロットします
    x = data['imageRate']
    y = data['sales']
    
    res1=np.polyfit(x, y, 1)
    #res3=np.polyfit(x, y, 3)
    
    res = x.corr(y)
    print(res1)
    print(res)
    #print(res3)
    
    y1 = np.poly1d(res1)(x)
    #y3 = np.poly1d(res3)(x)
    
    plt.plot(x, y1, label='fitted d=1', color='red')
    #plt.plot(x, y3, label='fitted d=3', color='green')
    plt.scatter(x,y,label='data')
    
    plt.title('Relationship between imageRate and Sales')
    plt.ylabel('Sales')
    plt.xlabel('imageRate')
    
    plt.grid(linestyle='dashed')
    plt.legend()
    plt.ylim([0,10000])
    plt.savefig("../fig/imageRateSales.png")
    plt.close()
    #print("Generate ../fig/getPriceSalesPlot.png")

getPriceSalesPlot()
