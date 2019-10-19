import sys
length = []

for i in range(len(sys.argv)):
	print('Argv of ' + str(i) + ' is ' + sys.argv[i])
	length.append(sys.argv[i])

length.sort(key=len, reverse=True)
for i in range(len(length)):
	print(length[i])