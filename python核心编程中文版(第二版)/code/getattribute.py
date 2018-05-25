# -*- coding:utf-8 -*-
"""
@project = 1
@file = getattribute
@author = Liangjisheng
@create_time = 2018/3/28 0028 下午 18:17
"""


class Test(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        if item == 'address':
            return 'China'


if __name__ == '__main__':
    test = Test('letian')
    print(test.name)
    print(test.address)
    test.address = 'anhui'
    print(test.address)


class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as ex:
            print(ex)

    def __getattr__(self, item):
        return 'default'


at = AboutAttr('test')
print(at.name)
# 上面例子里面的getattr方法根本不会被调用，因为原本的AttributeError被我们自行处理并未抛出，
# 也没有手动调用getattr，所以访问not_existed的结果是None而不是default
print(at.not_existed)
