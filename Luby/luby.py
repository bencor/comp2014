#Benjamin Correal
#Competition informatique 2014

N,t=[int(i) for i in raw_input().split()]

requiredTime=0
i=0
while 1<<i <= N:
	i+=1
while i > 0:
	j=(1<<i)-1
	if N>=j:
		N-=j
		requiredTime+=i*1<<(i-1)
	else:
		i-=1
	
curr_time=t
#sumLuby: [(sum, length)]
sumLuby=[(1,1)]
i=1
while sumLuby[-1][0] <= t:
	sumLuby.append((2*sumLuby[-1][0]+(1<<i),(1<<i+1)-1))
	i+=1

n=0
for i in xrange(len(sumLuby)-1,-1,-1):
	nb=min(2,t/sumLuby[i][0])
	n+=nb*sumLuby[i][1]
	t-=nb*sumLuby[i][0]
	if t==0 or nb>1: break

print n, requiredTime-curr_time