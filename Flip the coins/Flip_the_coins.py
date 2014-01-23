from math import sqrt

x = int(raw_input())
#Find primes under x
prime_test_range = x
isPrimes = range(prime_test_range + 1)
isPrimes[1] = 0
for i in xrange(2, int(sqrt(prime_test_range)) + 1):
	if isPrimes[i] == 0: continue
	for j in xrange(i * 2, prime_test_range + 1, i):
		isPrimes[j] = 0
primes = [p for p in isPrimes if p != 0]
del isPrimes

def getNbFactors(n):
	nbFact = 1
	for i in xrange(len(primes)):
		power = 1
		while n % primes[i] == 0:
			n /= primes[i]
			power += 1
		nbFact *= power
		if n == 1:
			break
	return nbFact

square = 1
nbFactors = 1
n = 1
while nbFactors < x:
	n+=1
	square += 2*n - 1
	nbFactors = getNbFactors(square)

print square