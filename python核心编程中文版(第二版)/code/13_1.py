# -*- coding:utf-8 -*-
"""
@project = 1
@file = 13_1
@author = Liangjisheng
@create_time = 2018/3/23 0023 下午 20:02
"""


class AddrBookEntry(object):
    """address book entry class"""

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print('Created instance for:', self.name)

    def updatePhone(self, newph):
        self.phone = newph
        print('Updated phone# for:', self.name)


john = AddrBookEntry('John Doe', '123')
jane = AddrBookEntry('Jane Doe', '456')
print(john)
print(jane)

print(john.name)
print(john.phone)
print()


class EmplAddrBookEntry(AddrBookEntry):
    """Employee Address Book Entry class"""

    def __init__(self, nm: object, ph: object, id: object, em: object) -> object:
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print('Updated e-mail address for:', self.name)


john = EmplAddrBookEntry('John Doe', '123', 42, 'john@163.com')
print(john.name)
print(john.phone)
print(john.email)
print(john.empid)

print(dir(AddrBookEntry))
print(dir(EmplAddrBookEntry))
print(type(AddrBookEntry))
print(type(EmplAddrBookEntry))
print()

print(AddrBookEntry.__name__)
print(AddrBookEntry.__doc__)
print(AddrBookEntry.__dict__)
print()

print(EmplAddrBookEntry.__name__)
print(EmplAddrBookEntry.__doc__)
print(EmplAddrBookEntry.__dict__)
