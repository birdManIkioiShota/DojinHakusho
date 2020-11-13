# -*- coding: utf-8 -*-

import CaboCha

c=CaboCha.Parser()

sentence = "純粋な子狐さんを拾ったらとことん癒してくれて心が浄化する音声"

# 視覚的にわかりやすいフォーマット
print(c.parseToString(sentence))

# プログラム的に処理しやすいフォーマット
tree =  c.parse(sentence)
print(tree.toString(CaboCha.FORMAT_LATTICE))
