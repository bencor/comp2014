n=int(raw_input())

con=[1]
for i in xrange(1,n):
	ncon=[]
	lv=con[0]
	lc=1
	for j in con[1:]:
		if j==lv:
			lc+=1
		else:
			ncon.append(lc)
			ncon.append(lv)
			lv=j
			lc=1
	ncon.append(lc)
	ncon.append(lv)
	con=ncon
print ''.join(str(i) for i in con)