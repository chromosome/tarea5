import sys
from itertools import combinations
from itertools import permutations

def cheat_or_not(guesses):
	for guess, n1, n2 in guesses:
		print(guess)


for line in sys.stdin:
	t = int(line.strip())

	sys.stdin.readline()
	for _ in range(t):
		line = sys.stdin.readline()
		line = line.strip().split()
		guess1, n11, n21 = line[0], line[1], line[2]

		line = sys.stdin.readline()
		line = line.strip().split()
		guess2, n12, n22 = line[0], line[1], line[2]

		sys.stdin.readline()

		cheat_or_not(((guess1, n11, n21), (guess2, n11, n21)))
