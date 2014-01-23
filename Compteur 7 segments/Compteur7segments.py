#Benjamin Correal
#Competition informatique 2014

x=int(raw_input())
digitCount=[0]*10
transition=[0]*10
digitCount[0]=1
if x>0:	transition[0]=1
add1=0

digitValue=1
n=x
while n>0:
	d=n%10
	n/=10
	if n>0:
		add1+=1
	if n>1:
		digitCount[0]+=(n-1)*digitValue
		transition[0]+=(n-1)
	if n>0:
		for i in xrange(1,10):
			digitCount[i]+=n*digitValue
			transition[i]+=n

	if n>0 and d>0:
		digitCount[0]+=digitValue
		transition[0]+=1
	for i in xrange(1, d):
		digitCount[i]+=digitValue
		transition[i]+=1
	
	digitCount[d]+=x%digitValue+1
	digitValue*=10

digitSegmentCount=[6,2,5,5,4,5,6,3,7,6]
digitTransitionCost=[0,4,1,1,2,1,1,4,0,1]
print digitSegmentCount[0] + sum(digitSegmentCount[i]*digitCount[i]+digitTransitionCost[i]*transition[i] for i in xrange(10)) + digitSegmentCount[1]*add1
