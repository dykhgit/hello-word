# coding=utf8

import random

def simulate(n=1000000):
	if not isinstance(n, int):
		print 'error parameter,should be int'
		return 

	count=int(0)
	for i in xrange(n):
		if(random.random()<=0.5):
			count=count+1;
	return count*1.0/n
