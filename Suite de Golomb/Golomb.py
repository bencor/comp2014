#Benjamin Correal
#Competition informatique 2014

from Queue import Queue
x = int(raw_input())
if x <= 3:
	if x <= 0:
		print "Invalid Input."
	elif x == 1:
		print 1
	elif x == 2:
		print 2.5
	elif x == 3:
		print 4.5
	exit()

q = Queue()
q.put((2,1))
s=5
value=3
index=3

while index < x:
	n1, n2 = q.get()
	for j in range(n2):
		if n1<x-index:
			q.put((value, n1))
			s += n1 * value
			index += n1
			value += 1
		else:
			s += value * (x - index)
			index=x
			break

n = s - value + 1;
moy = n + (value - 1) / 2.0
print repr(moy) if moy!=int(moy) else int(moy)