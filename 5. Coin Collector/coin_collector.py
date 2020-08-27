import sys

def collect(coins):
	
	acc = 0
	total = 1

	for i in range(1, len(coins)):
		if (acc+coins[i-1] < coins[i]):
			acc += coins[i-1]
			total += 1

	return total


for line in sys.stdin:
	cases = int(line.strip())

	for _ in range(cases):
		line = sys.stdin.readline()
		n = int(line.strip())

		line = sys.stdin.readline()
		coins = line.strip().split()
		coins = [ int(coin) for coin in coins ]

		print(collect(coins))
