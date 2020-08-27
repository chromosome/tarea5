import sys

# Analisis de complejidad -----------------------------------------------------
#
# Temporal: El algoritmo sigue una estrategia voraz en la que suma monedas a
# 			medida que las lee y son consideradas solo las monedas cuyo valor
# 			sea mayor que la suma parcial de los valores de las monedas 
# 			anteriores. Por lo tanto su complejidad es O(n).
#
# Espacial: El algoritmo trabaja sobre la cantidad de datos de entrada, por lo
# 			que en este caso se tiene complejidad O(n), pero puede modificarse
# 			para que lea elementos de a uno y obtener O(1).

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
