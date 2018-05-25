
#/usr/bin/env python

import urllib.request;
# from urllib import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():
			continue;
		else:
			return eachLine;
			
def firstLast(webpage):
	f = open(webpage);
	lines = f.readlines();
	f.close();
	print(firstNonBlank(lines));
	lines.reverse();
	print(firstNonBlank(lines));
	
def download(url = 'http://www', process = firstLast):
	try:
		retval = urllib.request.urlretrieve(url)[0];
	except IOError:
		print('IOError');
		retval = None;
	
	if retval:
		process(retval);
		
if __name__ == '__main__':
	download();