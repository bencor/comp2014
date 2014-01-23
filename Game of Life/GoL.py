import sys

import os
import time
import itertools

def printGoL(game):
	os.system('cls')
	if not game:
		return
	colOffset = min(0, min(list(itertools.chain.from_iterable(game.values()))))
	rows = list(game.keys())
	rows.sort()
	previousRow = min(0, rows[0])
	for i in rows:
		if previousRow + 1 < i:
			print '\n' * (i - previousRow - 1),
		previousRow = i
		game[i].sort()
		line = ' ' * (game[i][0] - colOffset) + chr(254)
		for j in range(1,len(game[i])):
			line += ' ' * (game[i][j] - game[i][j-1] - 1) + chr(254)
		print line

#stable
#startPattern = {3: [2, 3], 4:[2, 3]}
#DieHard
#startPattern = {5:[8], 6:[2, 3], 7:[3, 7, 8, 9]}
#Pulsar (period 3)
#startPattern = {2: [4, 5, 6, 10, 11, 12], 4: [2, 7, 9, 14], 5: [2, 7, 9, 14], 6: [2, 7, 9, 14],
#				7: [4, 5, 6, 10, 11, 12], 9: [4, 5, 6, 10, 11, 12], 10: [2, 7, 9, 14], 
#				11: [2, 7, 9, 14], 12: [2, 7, 9, 14], 14: [4, 5, 6, 10, 11, 12]}

#Glider
#startPattern = {1:[2],2:[3], 3:[1,2,3]}


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
for line in sys.stdin:
	addAlive(*[int(i) for i in line.split(' ')], game=startPattern)


startPatternList = sorted(startPattern.items())
currentGame = startPattern.copy()
nextGame = {}
for row in currentGame.values():
		row.sort()
#printGoL(currentGame)

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
	
	#printGoL(currentGame)
	if not currentGame:
		print "mourante", nIter
		break
	
	if len(currentGame) == len(startPattern):
		diff = None
		isSamePattern = True
		for pair in zip(sorted(currentGame.items()), startPatternList):
			if len(pair[0][1]) != len(pair[1][1]):
				isSamePattern = False
				break
			rowDiff = pair[0][0] - pair[1][0]
			for i in range(len(pair[0][1])):
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
			
	# nIter
	#time.sleep(1)
