import sys

# Analisis de complejidad -----------------------------------------------------
#
# Temporal: El algoritmo sigue una estrategia voraz en la que suma los 
# 			resultados de las apuestas a medida que se hacen, luego al momento
# 			de perder todo el dinero se termina la racha y se guarda su valor
# 			maximo. Esto se hace para todas las apuestas y se compara el valor
#			maximo de cada racha. Como actua sobre cada uno de los elementos de
# 			entrada se tiene una complejidad de O(n).
#
# Espacial: El algoritmo trabaja sobre la cantidad de datos de entrada, por lo
# 			que en este caso se tiene complejidad O(n), pero puede modificarse
# 			para que lea elementos de a uno y obtener O(1).

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

