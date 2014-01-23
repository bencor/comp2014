#Benjamin Correal
#Competition informatique 2014

from sys import stdin
m,n=[int(i) for i in raw_input().split()]
pos=[(int(coords[0]), int(coords[1])) for coords in (line.split() for line in stdin)]
print sum(min(m-i,n-j,*(max(p[0]-i,p[1]-j) for p in pos if p[0]>=i and p[1]>=j)) for i in xrange(m) for j in xrange(n))

#Le code en commentaire suivant peut remplacer la ligne 4.
#Il est laisse ici pour aider a la comprehension de ceux qui sont moins families avec Python.

#total = 0
#for i in range(m):
#	for j in range(n):
#		maxSizes = (max(p[0]-i, p[1]-j) for p in pos if p[0] >= i and p[1] >= j)
#		total += min(m-i, n-j,*maxSizes)
#print total