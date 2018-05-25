
# except

import sys;

try :
	f = open("myfile.txt");
	s = f.readline();
	i = int(s.strip());
except OSError as err:
	print("OS error: {0}".format(err));
except ValueError :
	print("Counld not convert data to an integer");
except:
	print("Unexcepted error: ", sys.exc_info()[0]);
	raise;
	
def this_fails():
	x = 1 / 0;
	
try : 
	this_fails();
except ZeroDivisionError as err:
	print("Handing run-time error: ", err);
	
# raise语句抛出一个指定的异常
# raise NameError("HiThere");

# 如果你只想知道这是否抛出了一个异常，并不想去处理它，
# 那么一个简单的 raise 语句就可以再次把它抛出
try :
	raise NameError("HiThere");
except NameError:
	print("An exception flew by");
	raise;