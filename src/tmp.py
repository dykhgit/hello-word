import math

def fun(n):
	if not isinstance(n, int):
		print 'parameter error'
		return

	arr=[i for i in xrange(1,n+1)]
	result=0;
	for i in arr:
		result=result+i;
	return result;

def isPrime(n):
	if not isinstance(n, int):
		print 'parameter error'
		return
	k=int(math.sqrt(n))
	stop=False
	for i in xrange(2,k+1):
		if n%i==0:
			stop=True
			break
	return not stop

if __name__=="__main__":
	pass