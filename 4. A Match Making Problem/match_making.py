import sys

def handle_input_set(B, S, case_count):
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
		handle_input_set(B, S, case_count)

	case_count += 1
