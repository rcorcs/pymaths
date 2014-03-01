import fractions
import math
import cmath
	
#euler 12
def triangle(n):
	#sum = 0
	#for i in range(1, n+1):
	#	sum += i
	return n*(n+1)/2

#euler 12
def get_divisor(n):
	if (n%2==0) and (n>2):
		return 2
	for i in range(3, (int(math.sqrt(n))+1)):
		if n%i==0:
			return i
		i += 1
	return 0

#euler 12, 32
def divisors(n):
	d = []
	for i in range(1, n+1):
		if(n%i==0):
			d.append(i)
	return d

#euler 12
def factors(n):
	factors = []
	temp = []
	d = get_divisor(n)
	if d!=0:
		temp.append(d)
		n = n/d
	else:
		factors.append(n)
		if len(temp)>0:
			n = temp.pop()
		else:
			n = 0
	while n!=0:
		d = get_divisor(n)
		if d!=0:
			temp.append(d)
			n /= d
		else:
			factors.append(n)
			if len(temp)>0:
				n = temp.pop()
			else:
				n = 0
	return factors

#euler 20
def factorial(n):
	fact = 1;
	while n>1:
		fact *= n;
		n -= 1;
	return fact;

#euler 21, 23
def sum_divisors(n):
	if n>1:
		s = 1
	else:
		s = 0
	if(n%2==0):
		for i in range(2, n, 1):
			if n%i==0:
				s += i
	else:
		for i in range(3, n, 2):
			if n%i==0:
				s += i
	return s

#euler 21
def amicable(n):
	b = sum_divisors(n)
	a = sum_divisors(b)
	return a==n and a!=b

#euler 23
def perfect(n):
	return n==sum_divisors(n)

#euler 23
def deficient(n):
	return sum_divisors(n)<n

#euler 23
def abundant(n):
	return sum_divisors(n)>n

#euler 27
def prime(n):
	isPrime = True
	d = 3
	if n<2:
		return False
	sqrt_n = math.sqrt(int(n))
	if n>2:
		if n%2==0:
			isPrime = False
		else:
			while(d<=sqrt_n):
				if n%d==0:
					isPrime = False
					break
				d = d + 2
	else:
		if n!=2:
			isPrime = False
	return isPrime

#euler 32
def pandigital(n):
	nstr = str(n)
	arr = [ s.isdigit() and int(s)>0 for s in set(nstr) ]
	return sum(arr)==9

#euler 36
def base2(n):
	binary = ''
	while(n>0):
		binary = str( n%2 ) + binary
		n = n/2
	return binary

#euler 36
def palindrome(s):
	isPalindrome = True
	slen = len(s)
	for i in range(slen):
		if s[i]!=s[slen-(i+1)]:
			isPalindrome = False
			break
	return isPalindrome

#euler 37
def left_truncate(n):
	s = str(n)
	if len(s)>1:
		return int(s[1:])
	else:
		return -1

#euler 37
def right_truncate(n):
	s = str(n)
	slen = len(s)
	if slen>1:
		return int(s[:slen-1])
	else:
		return -1

#euler 37
def truncatable_prime(n):
	if pymaths.prime(n):
		ntrunc = left_truncate(n)
		while pymaths.prime(ntrunc):
			ntrunc = left_truncate(ntrunc)
			if ntrunc<0:
				break

		if ntrunc>=0:
			return False

		ntrunc = right_truncate(n)
		while pymaths.prime(ntrunc):
			ntrunc = right_truncate(ntrunc)
			if ntrunc<0:
				break

		if ntrunc>=0:
			return False
		else:
			return True
	return False

#euler 92
def chain(n):
	finished = False
	nstr = str(n)
	nlen = len(nstr)
	c = [n]
	while not finished:
		s = 0
		for i in range(nlen):
			s = s + int(nstr[i])**2

		finished = s==1 or s==89
		c.append(s)
		nstr = str(s)
		nlen = len(nstr)		
	return c

#euler 243
def gcd(a,b): 
		"Euclid's Algorithm for Greatest Common Divisor" 
		while b: 
			a, b = b, a % b 
		return a 

#euler 243
def totient(n): 
	""" 
	Euler's totient or phi function: Compute the number of
	positives < n that are relatively prime to n
	""" 
	tot, pos = 0, n-1 
	while pos>0: 
		if fractions.gcd(pos,n)==1: tot += 1 
		pos -= 1 
	return tot 

#euler 243
def resilience(x):
	return totient(x) / (x - 1.0)

def root(x, y):
	return math.exp(1.0/y)**math.log(x)

def croot(x, y):
	return cmath.exp(1.0/y)**cmath.log(x)

def cpow(x,y):
	return cmath.exp(y*cmath.log(x))

def pi(n):
	s = 0
	for i in range(1, n+1):
		s += math.sqrt(float(n**2-4*(i**1)+2*i-1))/float(n**2)
	return 4*s

