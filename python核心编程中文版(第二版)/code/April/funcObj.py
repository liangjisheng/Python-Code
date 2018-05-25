# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = funcObj
@author = Liangjisheng
@create_time = 2018/4/5 0005 上午 10:37
"""
# 使得类的实例可调用，重载__call__()


class C(object):
    def __call__(self, *args, **kwargs):
        print("I'm callable! Called with args:\n", args, '\n', kwargs)


c = C()
# callable判断一个对象是否可调用
print(callable(C))  # 类是可调用的，调用完后生成一个类的实例
print(callable(c))
c()
c(3)
c(3, 4)
c(3, 4, x=1)
print()

# 可求值表达式
eval_code = compile('100 + 200', '', 'eval')
print(eval(eval_code))
# 单一可执行语句
single_code = compile('print("hello, world")', '', 'single')
print(single_code)
exec(single_code)
# 可执行语句组
exec_code = compile("""
req = int(input('Count how many numbers?'))
for eachNum in range(req):
    print(eachNum)
""", '', 'exec')
exec(exec_code)
print()

print(globals())
print(locals())

aString = input('input:')
print(aString)
if isinstance(aString, str):
    print('%s' % aString)
    print('%r' % aString)
print(type(aString))
