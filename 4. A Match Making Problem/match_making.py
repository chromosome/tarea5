import sys

# Analisis de complejidad -----------------------------------------------------
#
# Temporal: En este caso lo unico que se necesita hacer es obtener la cantidad
# 			de soleros al final del emparejamiento, por lo tanto solo es 
# 			necesario obtener los solteros que sobran al acabarse las solteras
# 			por lo tanto se tiene una complejidad O(n) sobre la entrada.
#
# Espacial: Se procesan los datos de entrada uno a la vez por lo que nunca se
# 			trabaja con mas de uno, por lo tanto su complejidad espacial es 
# 			O(1).

def match(B, S, case_count):
	remaining = B - S if B - S >= 0 else 0
	b = 61
	for _ in range(B):
		age = int(sys.stdin.readline())
		b = age if age < b else b

	for _ in range(S):
		sys.stdin.readline()

	if remaining == 0:
		print("Case {}: 0".format(case_count))
	else:
		print("Case {}: {} {}".format(case_count, remaining, b))

case_count = 1
for line in sys.stdin:
	B, S = line.strip().split()
	B, S = int(B), int(S)

	if B != 0 and S != 0:
		match(B, S, case_count)

	case_count += 1
