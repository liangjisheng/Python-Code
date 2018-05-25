# -*- coding:utf-8 -*-
"""
@project = 1
@file = getattr
@author = Liangjisheng
@create_time = 2018/3/28 0028 下午 17:56
"""

# __getattr__只作用于不存在的属性


class UrlGenerator(object):
    def __init__(self, root_url):
        self.url = root_url

    def __getattr__(self, item):
        if item == 'get' or item == 'post':
            print(self.url)
        return UrlGenerator('{}/{}'.format(self.url, item))


# 充分利用getattr会在没有查找到相应实例属性时被调用的特点，方便的通过链式调用生成对应的url
url_gen = UrlGenerator('http://xxxx')
url_gen.users.show.get


class Test(object):
    def __init__(self, name):
        self.name = name

    # 调用未定义的属性，返回一个值或者AttributeError异常
    def __getattr__(self, item):
        if item == 'address':
            return 'China'
        else:
            return 'UnKnown'


if __name__ == '__main__':
    test = Test('letian')
    print(test.name)
    print(test.address)
    print(test.asdf)
    test.address = 'Anhui'
    print(test.address)


class Test1(object):
    def __init__(self, name):
        self.name = name

    # 如果调用了类中一个未定义的方法，__getattr__也要返回一个方法
    def __getattr__(self, item):
        return len


if __name__ == '__main__':
    test = Test1('letian')
    print(test.getlength('letian'))
