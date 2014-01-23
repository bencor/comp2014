import sys

n=8
#n=int(raw_input())
pos=[]
testinput = ["2 3","5 5"]
#testinput = ["1 2","3 5", "5 1"]
#for line in sys.stdin:
for line in testinput:
	coords = line.split(' ')
	pos.append((int(coords[0]), int(coords[1])))
#print pos

total = 0
#test=[0]*n
for i in range(n):
	for j in range(n):
		d = [max(p[0]-i, p[1]-j) for p in pos if p[0] >= i and p[1] >= j]
		if len(d) == 0:
			d = min(n-i, n-j)
		else:
			d = min(min(d), n-i, n-j)
		#print i, j, d
		total += d
		#for t in range(d):
		#	test[t]+=1

print total
#print test