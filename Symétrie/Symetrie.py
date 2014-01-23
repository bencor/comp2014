#Benjamin Correal
#Competition informatique 2014

from sys import stdin
from math import sqrt, asin, pi
from collections import Counter

pts=[tuple([float(i) for i in line.split(' ')]) for line in stdin ]

#Les points sont consideres egaux si leurs valeurs arondies a 'roundDigit' decimales sont egales.
roundDigit=4
def roundEqual(x,y):
	return round(x,roundDigit) == round(y,roundDigit)
def roundEqualV(v1,v2):
	return len(v1)==len(v2) and all(roundEqual(v1[i],v2[i]) for i in range(len(v1)))

def calcDistSquare(a,b):
	dx,dy=(b[0]-a[0]),(b[1]-a[1])
	return round(dx*dx + dy*dy, roundDigit)

#Filtre les points qui ne sont pas susseptibles d'etre parmi les plus eloignes.
#Determine borne inferieure B correspondant a une distance entre 2 points eloignes, puis elimine les points qui sont a une distance < B de tous les autres points.
#En general, plus de 95% des points sont filtres pour une distribution aleatoire uniforme des points. Il existe des cas particuliers ou rien n'est filtre.
#Cette partie n'est vraiment utile qu'a partir de quelques milliers de points, ce qui depasse largement les besoins de la competition.
def farPointsFilter(pts):
	minX, maxX = min(pt[0] for pt in pts), max(pt[0] for pt in pts)
	minY, maxY = min(pt[1] for pt in pts), max(pt[1] for pt in pts)
	dx, dy = maxX-minX, maxY-minY
	margin=0.01
	marginX, marginY=margin*dx, margin*dy
	minXPts, maxXPts=[pt for pt in pts if pt[0]-minX<marginX], [pt for pt in pts if maxX-pt[0]<marginX]
	minYPts, maxYPts=[pt for pt in pts if pt[1]-minY<marginY], [pt for pt in pts if maxY-pt[1]<marginY]
	getX, getY = lambda pt:pt[0], lambda pt:pt[1]
	squareLowerBound=max(calcDistSquare(min(minXPts, key=getY), max(maxXPts,key=getY)),
						 calcDistSquare(max(minXPts, key=getY), min(maxXPts,key=getY)), 
						 calcDistSquare(min(minYPts, key=getX), max(maxYPts,key=getX)), 
						 calcDistSquare(max(minYPts, key=getX), min(maxYPts,key=getX)))
	corners=[(minX,minY), (minX,maxY), (maxX,minY), (maxX,maxY)]
	return [pt for pt in pts if any(calcDistSquare(c,pt)>=squareLowerBound for c in corners)]

filteredPts=farPointsFilter(pts)
pairs=[(filteredPts[i],filteredPts[j]) for i in range(len(filteredPts)-1) for j in range(i+1, len(filteredPts))]
dist={pair:calcDistSquare(*pair) for pair in pairs}
maxDist=max(dist.values())
farPts=list({pt for pair in pairs if roundEqual(dist[pair],maxDist) for pt in pair})
center=(sum([x for x,y in farPts])/len(farPts), sum([y for x,y in farPts])/len(farPts))
middlePts=[pt for pt in {((farPts[i][0]+farPts[j][0])/2, (farPts[i][1]+farPts[j][1])/2) for i in range(len(farPts)-1) for j in range(i+1, len(farPts))} if not roundEqualV(pt,center)]

def orient(v):
	(x,y)=v
	if x < 0:
		x,y	=-x,-y
	elif x==0 and y<0:
		y=-y
	return (x,y)

def vunit(pt1,pt2):
	x=pt2[0]-pt1[0]
	y=pt2[1]-pt1[1]
	n=sqrt(x**2 + y**2)
	return orient((x/n, y/n))

def validateAxis(pts, center, u):
	if u==(0,0):
		return False
	pt2=(center[0]+u[0],center[1]+u[1])
	dist = [(calcDistSquare(pt,center), calcDistSquare(pt,pt2)) for pt in pts if not roundEqualV(pt,center) and not roundEqualV(vunit(pt,center),u)]
	if len(dist)%2==1:
		return False
	distCount=Counter(dist)
	return all(count%2==0 for count in distCount.values())

def perpendicular(v):
	return orient((-v[1]+0,v[0])) # +0 is used to avoid '-0.0'

testAxis = {vunit(center,pt) for pt in farPts+middlePts if pt[0]>center[0] or (pt[0]==center[0] and pt[1]>center[1])}
testAxis.update([perpendicular(axis) for axis in testAxis])
validAxis=[axis for axis in testAxis if validateAxis(pts, center, axis)]
axisDeg = sorted(list({round(asin(v[1])*180/pi,3) for v in validAxis}))

if len(axisDeg)>0:
	print ' '.join('{:.3f}'.format(deg) for deg in axisDeg)
else:
	print "Aucun"