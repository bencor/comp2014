a,b=[int(i) for i in raw_input().split()]
n=[int(i) for i in raw_input().split()]
d1=n[0]
d2=n[1] if len(n)>1 else d1

if b == 0:
	print -1
	exit()

d=[]
a%=b
for i in xrange(1,d2+1):
	a*=10
	if i>=d1:
		d.append(a/b)
	a%=b

print sum(d)