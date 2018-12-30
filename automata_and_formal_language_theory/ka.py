def ka(x, stage=0):
	try:
		if stage == 0:
			if x[0] == '+':
				return ka(x[1:], 1)

		elif stage == 1:
			if x[0:2] == 'a+':
				return ka(x[2:], 2)
			elif x[0] == '-':
				return ka(x[1:], 3)

		elif stage == 2:
			if x[0] == 'b':
				return ka(x[1:], 2)
			elif x[0] == '-':
				return ka(x[1:], 1)

		elif stage == 3:
			if not len(x):
				return 'YES'

	except:
		pass

	return 'NO'

print(ka(input()))`