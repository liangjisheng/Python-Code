# -*- coding:utf-8 -*-
"""
@project = 0409-1
@file = queue_1
@author = Liangjisheng
@create_time = 2018/4/10 0010 下午 19:42
"""
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
q = Queue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
print()

q = LifoQueue()
for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
print()


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        return

    def __lt__(self, other):
        return self.priority < other.priority


q = PriorityQueue()
q.put(Job(5, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

while not q.empty():
    next_job = q.get()
    print('Processing job', next_job.description)
