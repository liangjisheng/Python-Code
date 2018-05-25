
# 列表解析的一个不足就是必需生成所有的数据, 用以创建整个列表. 这可能对有大量数据的迭
# 代器有负面效应. 生成器表达式通过结合列表解析和生成器解决了这个问题
# 生成器表达式在 Python 2.4 被引入, 它与列表解析非常相似，而且它们的基本语法基本相同;
# 不过它并不真正创建数字列表, 而是返回一个生成器，这个生成器在每次计算出一个条目后，把这
# 个条目“产生” (yield)出来. 生成器表达式使用了"延迟计算"(lazy evaluation), 所以它在使用
# 内存上更有效. 我们来看看它和列表解析到底有多相似

# 列表解析
# [expr for iter_var in iterable if cond_expr]
# 生成器表达式
# (expr for iter_var in iterable if cond_expr)

# 生成器并不会让列表解析废弃, 它只是一个内存使用更友好的结构, 
# 基于此, 有很多使用生成器地方

rows = [1, 2, 3, 17];

# 每调用一次cols(),函数会走到下一个yield处，并将对应的对象返回
def cols():
	"""example of simple generator"""
	yield 56;
	yield 2;
	yield 1;
	
# 不需要创建新的列表，直接就可以创建配对，使用下面的生成器表达式
x_product_pairs = ((i, j) for i in rows for j in cols());

# 现在我们可以循环 x_product_pairs , 它会懒惰地循环 rows 和 cols
for pair in x_product_pairs:
	print(pair);