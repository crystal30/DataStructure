#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SST import SST, SST1
from BST1 import BST
import datetime

#统计词频，才开始words = ['name', 'list', 'python', 'li', 'li', 'brid'] * 10000，可能是不同的单词太少，显示不出二叉树的优势
# 结果：
# 20000
# 10000
# 0:00:00.426781
# 20000
# 10000
# 0:00:00.228819
# 20000
# 10000
# 0:00:00.268810

#找一本书试试？
#二分搜索树，词频统计：时间复杂度O（logn）
bst = BST()
words = ['name', 'list', 'python', 'li', 'li', 'brid'] * 10000

start = datetime.datetime.now()
for word in words:
    value = bst.search(word)
    if value == None:
        bst.insert(word, 1)
    else:
        bst.insert(word, value + 1)
end = datetime.datetime.now()
print(bst.search('li'))
print(bst.search('brid'))
print(end - start)

#########无序链表组成的SST
sst = SST()
words = ['name', 'list', 'python', 'li', 'li', 'brid'] * 10000

start = datetime.datetime.now()
for word in words:
    value = sst.search(word)
    if value == None:
        sst.insert(word, 1)
    else:
        sst.insert(word, value + 1)
end = datetime.datetime.now()
print(sst.search('li'))
print(sst.search('brid'))
print(end - start)

#########有序链表组成的SST
sst1 = SST1()
words = ['name', 'list', 'python', 'li', 'li', 'brid'] * 10000

start = datetime.datetime.now()
for word in words:
    value = sst1.search(word)
    if value == None:
        sst1.insert(word, 1)
    else:
        sst1.insert(word, value + 1)
end = datetime.datetime.now()
print(sst1.search('li'))
print(sst1.search('brid'))
print(end - start)

