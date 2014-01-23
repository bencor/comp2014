#Benjamin Correal
#Competition informatique 2014

from sys import stdin

def isAlive(pos):
	if pos[0] not in currentGame.keys():
		return False
	return pos[1] in currentGame[pos[0]]

def addAlive(row, column, game):
	if row in game.keys():
		game[row].append(column)
	else:
		game[row] = [column]

startPattern={}
for line in stdin:
	addAlive(*[int(i) for i in line.split()], game=startPattern)

startPatternList = sorted(startPattern.items())
currentGame = startPattern.copy()
nextGame = {}
for row in currentGame.values():
		row.sort()

nIter = 0
while True:
	nIter += 1
	nextGame = {}
	potentialNewCell = {}
	for i in currentGame.keys():
		for j in currentGame[i]:
			nbAliveCell = 0
			neighbourCell = [(i-1, j-1), (i-1, j), (i-1, j+1), 
							 (i, j-1),               (i, j+1), 
							 (i+1, j-1), (i+1, j), (i+1, j+1)]
			
			for cell in neighbourCell:
				if isAlive(cell):
					nbAliveCell+=1
				else:
					if cell in potentialNewCell:
						potentialNewCell[cell]+=1
					else:
						potentialNewCell[cell]=1
			
			if nbAliveCell == 2 or nbAliveCell == 3:
				addAlive(i, j, nextGame)
			
	for cell in [c for c in potentialNewCell.keys() if potentialNewCell[c] == 3]:
		addAlive(cell[0], cell[1], nextGame)
	
	currentGame = nextGame
	for row in currentGame.values():
		row.sort()
	
	if len(currentGame) == len(startPattern):
		diff = None
		isSamePattern = True
		for pair in zip(sorted(currentGame.items()), startPatternList):
			if len(pair[0][1]) != len(pair[1][1]):
				isSamePattern = False
				break
			rowDiff = pair[0][0] - pair[1][0]
			for i in xrange(len(pair[0][1])):
				d = (rowDiff, pair[0][1][i] - pair[1][1][i])
				if diff and diff != d:
					isSamePattern = False
					break
				else:
					diff = d
		if isSamePattern:
			if nIter == 1:
				print "stable"
			else:
				if diff == (0, 0):
					print "periodique", nIter
				else:
					print "vaisseau", nIter, diff[0], diff[1]
			break
