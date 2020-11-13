# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import japanize_matplotlib
import time
import networkx as nx

def getCo_OccNet():
    data = pd.read_csv("../data/raw_data.csv", index_col='id')
    tagData = pd.read_csv("../data/getTagData.csv", index_col=0)
    tagList = tagData.index

    # とりあえず全部の性癖同士をくっつけるやーつ
    relation = pd.DataFrame({'from':[tagList[0]],'to':[tagList[1]]})
    k = 1
    for i in tagList:
        for j in tagList:
            if(i != j):
                flag = 0
                if(True in ((relation['from'] == j) & (relation['to'] == i)).values):
                    flag = 1
                if(flag == 0):
                    if(True in ((relation['from'] == i) & (relation['to'] == j)).values):
                        flag = 1
                
                if(flag==0):
                    tag = pd.DataFrame({'from':[i], 'to':[j]}, index=[k])
                    k = k + 1
                    relation = pd.concat([relation, tag])
    
    # 共起関係数算出するやーつ
    print(relation)
    jaccard = None
    co_occ = None
    spl_tag = data['tag'].str.split(',', expand=True)
    k = 0
    for r_index, r_row in relation.iterrows():
        sizeofA = 0
        sizeofB = 0
        sizeofAandB = 0
        sizeofAorB = 0
        for index, row in spl_tag.iterrows():
            counter = 0
            if((row==r_row['from']).sum() >= 1):
                sizeofA = sizeofA + 1
                counter = counter + 1 
            if((row==r_row['to']).sum() >= 1):
                sizeofB = sizeofB + 1
                counter = counter + 1
            if(counter == 2):
                sizeofAandB = sizeofAandB + 1
        both = pd.DataFrame({'sizeofFrom':[sizeofA], 'sizeofTo':[sizeofB],'sizeofFromandTo':[sizeofAandB]}, index=[k])
        k = k + 1
        co_occ = pd.concat([co_occ, both])
    print(co_occ)
    co_occ = pd.concat([relation, co_occ],axis=1)
    print(co_occ)
    co_occ.to_csv("../data/co_occ.csv")
    
start = time.time()
getCo_OccNet()
end = time.time()
print(end-start)
