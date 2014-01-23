from sys import stdin
m,n=[int(i) for i in raw_input().split()]
pos=[(int(coords[0]), int(coords[1])) for coords in (line.split() for line in stdin)]
print sum(min(m-i,n-j,*(max(p[0]-i,p[1]-j) for p in pos if p[0]>=i and p[1]>=j)) for i in range(m) for j in range(n))

#total = 0
#for i in range(m):
#	for j in range(n):
#		maxSizes = (max(p[0]-i, p[1]-j) for p in pos if p[0] >= i and p[1] >= j)
#		total += min(m-i, n-j,*maxSizes)
#print total