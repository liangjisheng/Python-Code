
#/usr/bin/env python

# 这个函数对象的引用计数在函数创建时被设置为True,但是因为没有引用保存下来
# 引用计数右回到0，然后被垃圾回收掉
print(lambda : True);

true = lambda : True;
print(true());

def usuallyAdd2(x, y = 2) : return x + y;
def showAllAsTuple(*z) : return z;

a = lambda x, y = 2 : x + y;
print(a(3));
print(a(3, 5));
print(a(0));
print(a(0, 9));

b = lambda *z : z;
print(b(23, 'zyx'));
print(b(42));
print();