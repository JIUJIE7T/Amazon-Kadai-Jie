sales = [(50.0,), (20.0,)]
flattened = []
for sublist in sales:
	for elements in sublist:
		flattened.append(elements)

print flattened