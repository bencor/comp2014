#Benjamin Correal
#Competition informatique 2014

n=int(raw_input())

conway=[1]
for i in xrange(1,n):
	nextconway=[]
	value=conway[0]
	count=1
	for j in conway[1:]:
		if j==value:
			count+=1
		else:
			nextconway.append(count)
			nextconway.append(value)
			value=j
			count=1
	nextconway.append(count)
	nextconway.append(value)
	conway=nextconway
print ''.join(str(i) for i in conway)