import sys

def filter(file):
	''' file -> array of string '''
	array = []
	for line in file:
	# 1. remove html tags
		for ch in ['/<','>/','</','/>']:
			line = line.replace(ch,"")
	array.append(line)
	print(array)

# computing filter function
if __name__ == "__main__":
	# read tweet corpus and put it on the array	
	f = open(sys.argv[1],'r')
	filter(f)


