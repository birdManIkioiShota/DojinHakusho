# -*- coding: utf-8 -*-

import CaboCha

c=CaboCha.Parser()

sentence = "僕は最愛の妻を部下に寝取られた。"

# 視覚的にわかりやすいフォーマット
print(c.parseToString(sentence))

# プログラム的に処理しやすいフォーマット
tree =  c.parse(sentence)
print(tree.toString(CaboCha.FORMAT_LATTICE))
