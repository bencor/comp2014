#Benjamin Correal
#Competition informatique 2014

from sys import stdin
from collections import defaultdict

lab = [line.replace("\n","") for line in stdin]
start=end=-1
for i in xrange(len(lab)):
	for j in xrange(len(lab[i])):
		if lab[i][j]=='1':
			start=(i,j)
			if end!=-1: break
		elif lab[i][j]=='2':
			end=(i,j)
			if start!=-1:break
	if start!=-1 and end!=-1: break

def neighbours(i,j):
	if i>0 and j<len(lab[i-1]):
		yield (i-1,j)
	if j+1<len(lab[i]):
		yield (i,j+1)
	if i+1<len(lab) and j<len(lab[i+1]):
		yield (i+1,j)
	if j>0:
		yield (i,j-1)

#dist is used as dist[(i,j)]=[{keys}]
dist=defaultdict(list)
curr_nodes=defaultdict(list)
curr_nodes[start].append(set())
k=0
while any(curr_nodes) and not end in curr_nodes:
	next_nodes=defaultdict(list)
	
	for ((i,j),keysList) in curr_nodes.items():
		for keys in keysList:
			for (ni,nj) in neighbours(i,j):
				if lab[ni][nj]=='#' or ('A'<=lab[ni][nj]<='Z' and lab[ni][nj].lower() not in keys): continue
				newKeys=keys.copy()
				if 'a'<=lab[ni][nj]<='z':
					newKeys.add(lab[ni][nj])
				if ((ni,nj) not in dist or not any(prevKeySet>=newKeys for prevKeySet in dist[(ni,nj)])) and ((ni,nj) not in next_nodes or newKeys not in next_nodes[(ni,nj)]):
					next_nodes[(ni,nj)].append(newKeys)
		
	for ((i,j),keysList) in curr_nodes.items():
		for keys in keysList:
			dist[(i,j)].append(keys)
	
	curr_nodes=next_nodes
	k+=1

if end in curr_nodes:
	print k
else:
	print "Impossible"