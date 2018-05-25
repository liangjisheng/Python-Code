# -*- coding:utf-8 -*-
"""
@project = 0520-1
@file = set_1
@author = Liangjisheng
@create_time = 2018/5/20 0020 上午 9:49
"""
name = set(['Tom', 'Lucy', 'Ben'])
print(name)
name.add('Juny')
print(name)
name.clear()
print(name)
name = set(['Tom', 'Lucy', 'Ben'])
new_name = name.copy()
print(new_name)

# difference(返回两个或多个集合中不同的元素，并生成新的集合)
A = set([2, 3, 4, 5])
B = set([3, 4])
C = set([2])
n = A.difference(B, C)
print(n)
# difference_update(删除A集合里面,在B集合中存在的元素)
A = set([2, 3, 4, 5])
B = set([4, 5])
A.difference_update(B)
print(A)
# discard(移除元素,如果元素不存在不报错)
n = set([2, 3, 4])
n.discard(3)
print(n)
# intersection(取交集，并生成新的集合)
n1 = set([2, 3, 4, 5])
n2 = set([4, 5, 6, 7])
n = n1.intersection(n2)
print(n)

# intersection_update(取交集，修改原来的集合)
n1 = set([2, 3, 4, 5])
n2 = set([4, 5, 6, 7])
n1.intersection_update(n2)
print(n1)
# isdisjoint(判断交集，是返回False，否返回True)
n1 = set([2, 3, 4, 5])
n2 = set([4, 5, 6, 7])
print(n1.isdisjoint(n2))
# issubset(判断子集)
A = set([2, 3])
B = set([2, 3, 4, 5])
print(A.issubset(B))
# issuperset(判断父集)
print(B.issuperset(A))

# pop(随机移除一个元素)
n = set([2, 3, 4, 5])
n1 = n.pop()
print(n, n1)
# remove(移除指定元素,元素不存在会报错)
n = set([2, 3, 4, 5])
n.remove(2)
print(n)

# A,B的补集减去A,B的交集
A = set([2, 3, 4, 5])
B = set([4, 5, 6, 7])
print(A.symmetric_difference(B))    # 生成新的集合
A.symmetric_difference_update(B)    # 原地操作
print(A)

#  union（取并集，并生成新的集合）
A = set([2, 3, 4, 5])
B = set([4, 5, 6, 7])
print(A.union(B))
# update(取并集，改变原来的集合)
A.update(B)
print(A)
