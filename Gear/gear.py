from math import sqrt
from operator import mul

gears = [int(i) for i in raw_input().split(' ')]

sieve_range = max(gears)
isPrimes = range(sieve_range + 1)
isPrimes[1] = 0
for i in xrange(2, int(sqrt(sieve_range)) + 1):
	if isPrimes[i] != 0:
		for j in xrange(i * 2, sieve_range + 1, i):
			isPrimes[j] = 0
primes = [p for p in isPrimes if p != 0]

def factorize(n):
	factors = [0] * len(primes)
	for i in xrange(len(primes)):
		while n % primes[i] == 0:
			n /= primes[i]
			factors[i] += 1
		if n == 1:
			break
	return factors

gearsFactors = [factorize(g) for g in gears]
totalFactors = [max(f) for f in zip(*gearsFactors)]
nbTurn = reduce(mul, [primes[i]**(totalFactors[i] - gearsFactors[0][i]) for i in range(len(primes))])

print nbTurn