
# 这个程序管理用于登录系统的用户信息：登录名字和密码。登录用户帐号建立后，已存在用户
# 可以用登录名字和密码重返系统。新用户不能用别人的登录名建立用户帐号

db = {};

def newuser():
	prompt = 'login desired: ';
	while True:
		name = input(prompt);
		if name in db:
			prompt = 'name taken, try another: ';
			continue;
		else:
			pwd = input('passwd: ');
			db[name] = pwd;
			break;
		
def olduser():
	name = input('login: ');
	pwd = input('passwd: ');
	passwd = db.get(name)
	if passwd == pwd:
		print('welcome back', name);
	else:
		print('login incorrect');
		
def showmenu():
	prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """
	done = False;
	while not done:
		chosen = False;
		while not chosen:
			try:
				choice = input(prompt).strip()[0].lower();
			except (EOFError, KeyboardInterrupt):
				choice = 'q';
			
			print('\nYou picked: [%s]' % choice);
			if choice not in 'neq':
				print('invalid option, try again');
			else:
				chosen = True;
		
		if choice == 'n':
			newuser();
		elif choice == 'e':
			olduser();
		elif choice == 'q':
			done = True;
		
if __name__ == '__main__':
	showmenu();