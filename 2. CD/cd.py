import sys

# Analisis de complejidad -----------------------------------------------------
#
# Temporal: Este problema es knapsack, pero con todos los valores iguales a su
# 			peso, por lo que se debe construir una tabla de n*W elementos donde
# 			W es el tamano del CD y n la cantidad de canciones. En este caso
# 			construir la tabla toma O(nW) y la reconstrucción de la solucion en
# 			base a la tabla es O(n). Por lo tanto su complejidad esta dominada
# 			por O(nW).
# 
# Espacial: Como se tiene que es el problema de knapsack se construye la tabla
# 			de n*W elementos por lo tanto se tiene una complejidad espacial de
# 			O(nW).

def knapsack(N, n, t):
	m = [ [0]*(N+1) for _ in range(n+1) ]
	t = t[::-1]
	v = t

	for i in range(1, n+1):
		for j in range(N+1):

			if t[i-1] > j:
				m[i][j] = m[i-1][j]

			else:
				m[i][j] = max(m[i-1][j], m[i-1][j-t[i-1]] + v[i-1])

	cd = []
	j = N
	for i in reversed(range(1, n+1)):
		# if m[i][j] != m[i-1][j]:
		if m[i][j] == m[i-1][j-t[i-1]] + v[i-1]:
			cd.append(t[i-1])
			j = j-t[i-1]

	return cd


for line in sys.stdin:
	line = line.strip().split()

	N = int(line[0])
	n = int(line[1])
	t = [ int(t) for t in line[2:] ]

	k = knapsack(N, n, t)
	cs = ' '.join(str(c) for c in k)
	print('{} sum:{}'.format(cs, sum(k)))
