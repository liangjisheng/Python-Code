# -*- coding:utf-8 -*-
"""
@project = 0401-1
@file = stack frame_1
@author = Liangjisheng
@create_time = 2018/4/1 0001 上午 9:47
"""
import dis
import inspect
frame = None


def foo():
    bar()


def bar():
    global frame
    # 保存当前帧对象到frame中
    frame = inspect.currentframe()


# 标准的python解释器是用C写的，解释器用一个叫PyEval_EvalFrameEx()的C函数来执行Python函数
# 它接受一个python堆栈帧对象，并在这个堆栈帧的上下文中执行python字节码
# 当 PyEval_EvalFrameEx 遇到 CALL_FUNCTION 字节码的时候，它会创建一个新的 Python 堆栈帧，
# 然后用这个新的帧作为参数递归调用 PyEval_EvalFrameEx 来执行 bar
# Python 的堆栈帧是分配在堆内存中的，理解这一点非常重要！Python 解释器是个普通的 C 程序，
# 所以它的堆栈帧就是普通的堆栈。但是它操作的 Python 堆栈帧是在堆上的。除了其他惊喜之外，
# 这意味着 Python 的堆栈帧可以在它的调用之外存活
print(dis.dis(foo))     # dis.dis()用来查看一个对象的字节码

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

