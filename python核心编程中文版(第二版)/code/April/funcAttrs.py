# -*- coding:utf-8 -*-
"""
@project = 0405-1
@file = funcAttrs
@author = Liangjisheng
@create_time = 2018/4/5 0005 上午 11:29
"""


def foo():
    return True


def bar():
    """bar() does not do much"""
    return True


foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print('PASSED')
else:
    print('FAILED')
'''

print(dir())

for eachAttr in dir():
    obj = eval(eachAttr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print('\nFunction "%s" has a doc string:\n\t%s' % (eachAttr, obj.__doc__))
        if hasattr(obj, 'tester'):
            print('Function "%s" has a tester... executing' % eachAttr)
            exec(obj.tester)
        else:
            print('Function "%s" has no tester... skipping' % eachAttr)
    else:
        print('"%s" is not a function' % eachAttr)

print(dir())
