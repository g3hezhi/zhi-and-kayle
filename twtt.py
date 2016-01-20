import sys

# read tweet corpus and put it on the array
array = []
f = open(sys.argv[1],'r')
for line in f:
	# 1. remove html tags
	for ch in ['/<','>/','</','/>']:
		line = line.replace(ch,"")
	# 2. replace html char with ASCII
	for ch in ['/<','>/','</','/>']:
		line = line.replace(ch,"")
	# 3.
	for ch in ['/<','>/','</','/>']:
		line = line.replace(ch,"")
	array.append(line)
print(array)

