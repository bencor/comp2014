sequence = sorted([int(i) for i in raw_input().split(' ')])

#Validate input
def gcd(a, b):
	if b == 0: 	return a
	else: 		return gcd(b, a % b)
	
commonDiv = sequence[0]
for x in sequence[1:]:
	commonDiv = gcd(commonDiv, x)
	if commonDiv == 1: break

if (commonDiv != 1) or any(i<=1 for i in sequence) or len(sequence)<2:
	print "Impossible"
	exit()
	
a=sequence[0]
b=next((i for i in sequence[1:] if gcd(a,i)==1),0)
if b==0:
	maxBound=sequence[len(sequence)-1]**2
else:
	maxBound = a*b-(a+b)
if len(sequence)==2:
	frobeniusNumber=maxBound
else:
	testRange=set(sequence)
	consecutive=0
	fn=a-1
	for i in xrange(a, maxBound+1):
		if i in testRange:
			consecutive+=1
			if consecutive >= a:
				break
			testRange.remove(i)
			for j in sequence:
				n=i+j
				if n<=maxBound:
					testRange.add(i+j)
		else:
			consecutive=0
			fn=i
	frobeniusNumber=fn
print frobeniusNumber