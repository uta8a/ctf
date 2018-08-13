__author__ = 'Robbie Barrat'

# Put the words you are trying to find here. All the text you enter should be 100% uppercase or 100% lowercase.

solutions = ['tjctf']

# Here goes your puzzle, separate each letter by a space.

import collections
import string

def caesar( rotate_string, number_to_rotate_by ):
	lower = collections.deque(string.lowercase)
	lower.rotate(number_to_rotate_by)
	lower = ''.join(list(lower))

	return rotate_string.translate( string.maketrans(string.lowercase, lower))

handle = open('a.txt')
original = handle.read()
handle.close()

open('solution.txt', 'w').write(caesar(original, 18))
exit()

for i in range(26):
	puzzle = caesar(original, i)
	print "permutation", i

	# Just formats the puzzle into a more computer-readable text
	wordgrid = puzzle.replace(' ','')

	# Computers start counting at zero, so...
	length = wordgrid.index('\n')+1


	characters = [(letter, divmod(index, length))
		    for  index, letter in enumerate (wordgrid)]

	wordlines = {}
	# These next lines just  directions so you can tell which direction the word is going
	directions = {'going downwards':0, 'going downwards and left diagonally':-1, 'going downwards and right diagonally':1}

	for word_direction, directions in directions.items():
	    wordlines[word_direction] = []
	    for x in range(length):
		for i in range(x, len(characters), length + directions):
		    wordlines[word_direction].append(characters[i])
		wordlines[word_direction].append('\n')

	# Nice neat way of doing reversed directions.
	wordlines['going right'] = characters
	wordlines['going left'] = [i for i in reversed(characters)]
	wordlines['going upwards'] = [i for i in reversed(wordlines['going downwards'])]
	wordlines['going upwards and left diagonally'] = [i for i in reversed(wordlines['going downwards and right diagonally'])]
	wordlines['going upwards and right diagonally'] = [i for i in reversed(wordlines['going downwards and left diagonally'])]


	def printitout(direction, tuple, lines):
	    # print "Keep in mind, rows are horizontal and columns are vertical.\n"
	    for direction, tuple in lines.items():
		string = ''.join([i[0] for i in tuple])
		for word in solutions:
		    if word in string:
		        coordinates = tuple[string.index(word)][1]
		        print word, 'is at row', coordinates[0]+1, 'and column', coordinates[1]+1, direction + "."

	printitout(word_direction, tuple, wordlines)
