import random
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph
from ReadGraph import ReadGraph
from UnicomComponent import UnicomComponent
from Path import Path
from ShortPath import ShortPath

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
r_sg2 = ReadGraph('graph2', SparseGraph)
r_sg2.show()
# u_c1 = UnicomComponent(r_sg1)
# print(u_c1.count())
# path = Path(r_sg2, 0)
# path.showPath(3)
sp = ShortPath(r_sg2, 0)
sp.showPath(4)
print(sp.length(0))
print(sp.length(2))
print(sp.length(5))
print(sp.length(6))
print(sp.length(3))
print(sp.length(4))






