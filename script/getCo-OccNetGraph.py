# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import networkx as nx

data = pd.read_csv("../data/co_occ.csv")
data = data.loc[data['sizeofFromandTo'] >= 20]

df = pd.DataFrame({'A':data['from'], 'B':data['to'], 'AandB':data['sizeofFromandTo']})
weighted_edgs = np.array(df)
edge_width = ((df['AandB'])**2)/100

G = nx.Graph()
G.add_weighted_edges_from(weighted_edgs)
pos = nx.spring_layout(G, k=20)
plt.figure()

nx.draw_networkx(G, pos, node_shape = "o", node_color = "c", node_size = 1500, font_family = "IPAexGothic")
nx.draw_networkx_edges(G, pos,edge_color = "gray", width = edge_width)
plt.title("Co-occurrence Network Graph of 陽向葵ゅか (weight >= 10)")
plt.show()
