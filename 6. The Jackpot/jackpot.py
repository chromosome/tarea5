import sys

def jackpot(bets):

	max_streak = 0
	streak = 0
	for bet in bets:

		streak += bet
		max_streak = streak if streak > max_streak else max_streak

		if streak < 0:
			streak = 0

	return max_streak



for line in sys.stdin:

	while line == '\n':
		line = sys.stdin.readline()

	if line.strip() == '0':
		break

	n = int(line.strip())
	bets = []
	while len(bets) < n:
		line = sys.stdin.readline()
		line = line.strip().split()
		for bet in line:
			bets.append(int(bet))


	s = jackpot(bets)

	if s:
		print("The maximum winning streak is {}.".format(s))
	else:
		print("Losing streak.")

