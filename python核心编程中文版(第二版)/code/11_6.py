
#/usr/bin/env python

# 使用tuple存储非关键字可变长参数,使用一个*号表示非关键字变长参数
def tupleVarArgs(arg1, arg2 = 'defaultB', *theRest):
	'display regular args and non-keyword variable args'
	print('formal arg1: ', arg1, sep = '');
	print('formal arg2: ', arg2, sep = '');
	for eachXtrArg in theRest:
		print('another arg: ', eachXtrArg, sep = '');
		
#tupleVarArgs('abc');
#tupleVarArgs(23, 4.56);
#tupleVarArgs('abc', 123, 'xyz', 456.789);

# 使用字典存储关键字变长参数,使用**表示关键字变长参数
def dictVarArgs(arg1, arg2 = 'defaultB', **theRest):
	'display 2 regular args and keyword variable args'
	print('formal arg1:', arg1);
	print('formal arg2:', arg2);
	for eachXtrArg in theRest.keys():
		print('Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg])));
		
#dictVarArgs(1220, 740.0, c = 'grail');
#dictVarArgs(arg2 = 'tales', c = 123, d = 'poe', arg1 = 'mystery');
#dictVarArgs('one', d = 10, e = 'zoo', men = ('freud', 'gaudi'));

# 关键字和非关键字参数都有可能用在同一个函数中，只要关键字字典是最后一个
# 参数并且非关键字元组先于它之前出现
def newfoo(arg1, arg2, *nkw, **kw):
	'display regular args and all variable args'
	print('arg1 is:', arg1);
	print('arg2 is:', arg2);
	for eachNKW in nkw:
		print('additional non-keyword arg:', eachNKW);
	for eachKW in kw.keys():
		print("additional keyword arg '%s' : '%s'" % (eachKW, str(kw[eachKW])));

newfoo('wolf', 3, 'projects', freud = 90, gamble = 96);
newfoo(2, 4, *(6, 8), **{'foo':10, 'bar':12});
print();

aTuple = (6, 7, 8);
aDict = {'z':9};
newfoo(1, 2, 3, x = 4, y = 5, *aTuple, **aDict);