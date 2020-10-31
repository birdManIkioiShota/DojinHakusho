# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import datetime as dt

def getTagBoxPlot():
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    
    # ここでタグを指定する
    data = data.query('tag.str.contains("ラブラブ/あまあま")', engine='python')
    
    fig, axes = plt.subplots()
    plt.boxplot(data['sales'], showmeans=True)
    plt.grid(linestyle='dashed')
    axes.set_xticklabels(["ラブラブ/あまあま"])
    plt.xlabel("ジャンル")
    plt.ylabel("sales")
    plt.title("Boxplot of sales (tag = ラブラブ/あまあま)")
    plt.ylim([0, 10000])
    plt.savefig("../fig/getTagBoxplot.png")

getTagBoxPlot()
