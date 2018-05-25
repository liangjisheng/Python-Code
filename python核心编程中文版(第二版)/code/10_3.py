
#!/usr/bin/env python

import os, socket, errno, types, tempfile;

class NetworkError(IOError):
	pass;
	
class FileError(IOError):
	pass;
	
def updArgs(args, newarg = None):
	if isinstance(args, IOError):
		myargs = [];
		myargs.extend([arg for arg in args]);
	else:
		myargs = list(args);
		
	if newarg:
		myargs.append(newarg);
	
	return tuple(myargs);
	
def fileArgs(file, mode, args):
	if args[0] == errno.EACCES and 'access' in dir(os):
		perms = '';
		permd = {'r':os.R_OK, 'w':os.W_OK, 'x':os.X_OK};
		pkeys = permd.keys();
		pkeys.sort();
		pkeys.reverse();
		
		for eachPerm in 'rwx':
			if os.access(file, permd[eachPerm]);
				perms += eachPerm;
			else:
				perms += '-';
	
		if isinstance(args, IOERROR):
			myargs = [];
			myargs.extend([arg for arg in args]);
		else:
			myargs = list(args);
		
		myargs[1] = "'%s' %s (perms: '%s')" %(mode, myargs[1], perms);
		
	else:
		myargs = args;
		
	return tuple(myargs);