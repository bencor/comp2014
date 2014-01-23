#Benjamin Correal
#Competition informatique 2014

binvalue = int(raw_input())
binrep=bin(binvalue)[2:]
len_prime = len(binrep)

prime_test_range = len_prime**2
isPrimes = range(prime_test_range + 1)
for i in xrange(2, len_prime + 1):
	if isPrimes[i] != 0:
		for j in xrange(i * 2, prime_test_range + 1, i):
			isPrimes[j] = 0
primes = [p for p in isPrimes if p != 0][:len_prime]

primevalue=sum([primes[i] for i in xrange(len_prime) if binrep[len_prime-1-i] == '1'])
del isPrimes, primes

fib = [1,2]
for i in xrange(0,primevalue):
	f=fib[i]+fib[i+1]
	if f > primevalue:
		break
	fib.append(f)

len_fib = len(fib)
fibrep=[0]*len_fib
v=primevalue
for i in xrange(len_fib):
	f=fib[len_fib-1-i]
	if v>=f and (i==0 or fibrep[i-1]==0):
		fibrep[i]=1
		v-=f
fibrepvalue=sum([1<<i for i in xrange(len_fib) if fibrep[len_fib-1-i]==1])

print ''.join([str(i) for i in fibrep])