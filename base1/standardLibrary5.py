
# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。
# Python 提供了一个度量工具，为这些问题提供了直接答案。
# 例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要
# 诱人的多,timeit 证明了现代的方法更快一些
# 相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了
# 针对更大代码块的时间度量工具

from timeit import Timer;

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit());

print(Timer('a,b = b,a', 'a=1; b=2').timeit());