
# 列表实现队列
queue = [];

# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
# str.strip([chars]);

def enQ():
	queue.append(input('Enter new string: ').strip());
	
def deQ():
	if len(queue) == 0:
		print('Cannot pop from an empty queue!');
	else:
		print('Removed [', queue.pop(0), ']');
		
def viewQ():
	print(queue);	# calls str() internally
	
CMDs = {'e':enQ, 'd':deQ, 'v':viewQ};

def showmenu():
	pr = """
(E)nqeuue
(D)equeue
(V)iew
(Q)uit

Enter choice: """
	
	while True:
		while True:
			try:
				choice = input(pr).strip()[0].lower();
			except (EOFError, KeyError, IndexError):
				choice = 'q';
			
			print('\nYou picked: [%s]' % choice);
			if choice not in 'devq':
				print('Invalid option, try again');
			else:
				break;
			
		if choice == 'q':
			break;
		
		CMDs[choice]();
		
if __name__ == '__main__':
	showmenu();