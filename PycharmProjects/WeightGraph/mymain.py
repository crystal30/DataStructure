import random
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph
from ReadGraph import ReadGraph
from UnicomComponent import UnicomComponent
from Path import Path
from ShortPath import ShortPath
from LazyPrimMST import LazyPrimMST
from Prim import PrimMST
from Kruskal import KruskalMST
from Dijkstra import Dijkstra
from BellmanFord import BellmanFord

# sg = SparseGraph(5, False)
# dg = DenseGraph(5, False)
# #随机生成节点数为5，边数为15的稀疏图（邻接表） 和 稠密图（邻接矩阵）
# for i in range(15):
#     v = random.randint(0, sg.V()-1)
#     w = random.randint(0, sg.V()-1)
#
#     sg.addEadge(v,w)
#     dg.addEadge(v,w)

# r_sg2 = ReadGraph('graph2', SparseGraph)
# r_sg2.show()
# u_c2 = UnicomComponent(r_sg2)
# print(u_c2.count())

print('------------')
r_sg1 = ReadGraph('graph4', SparseGraph, True)
r_sg1.show()
p = BellmanFord(r_sg1,0)
for i in range(1,r_sg1.V()):
    p.showPath(i)
# r_sg2 = ReadGraph('graph1', SparseGraph)
# r_sg2.show()

# [0.16, 0.19, 0.26, 0.17, 0.28, 0.35, 0.4]




