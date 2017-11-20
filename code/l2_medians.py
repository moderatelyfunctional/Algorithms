import math
import random

const = 20
sub_size = 5
def SELECT(S, i):
	if len(S) < const:
		return sorted(S)[i] # assuming rank is zero indexed
	num_medians = int(math.ceil(len(S) / sub_size))
	medians = []
	for curr_index in range(0, len(S), sub_size):
		sub = S[curr_index : min(curr_index + sub_size, len(S))]
		mid_index = int(math.floor(len(sub) / 2))
		medians.append(sorted(sub)[mid_index])

	median = SELECT(medians, int(math.floor(len(medians) / 2)))
	B = []
	C = []
	for element in S:
		if element < median:
			B.append(element)
		elif element > median:
			C.append(element)
	if len(B) == i:
		return median
	elif len(B) > i:
		return SELECT(B, i)
	else:
		return SELECT(C, i - len(B) - 1)

arr = range(40)
random.shuffle(arr)
print(arr)

print(SELECT(arr, 15))