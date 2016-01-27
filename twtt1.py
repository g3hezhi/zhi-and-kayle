import sys
import re

#### write help function that only take string/list as input, and output desired processed string##

#html tag and attribute removal
def task1(twtText):
	'''
	input = st = "Meet me today at the FEC in DC at 4. Wear a carnation so I know it��s you. \d href=Http://bit.ly/PACattack <a href=Http://bit.ly/PACattack ?> + ^ g"
	output = 'Meet me today at the FEC in DC at 4. Wear a carnation so I know it��s you. g'
	'''
	twtList = twtText.split()
	solu =""
	for i in twtList:
		if "<" in i or ">" in i or "/" in i or "\\" in i or "[" in i or "+" in i or "]" in i or "^" in i:
			continue
		else:
			solu += i+" "
	return solu.rstrip()

#not sure what to do here.
#def task2		

#URL removal : www or http
def task3(twtText):
	twtList = twtText.split()
	solu = ""
	for i in twtList:
		print(i)
		if i.lower().startswith("www.") or i.lower().startswith("http"):
			continue
		else:
			solu += i+" "
	return solu.rstrip()
			
# @ and # removeal
def task4(twtText):
	twtList = twtText.split()
	solu = ""
	for i in twtList:
		if i.startswith("@"):
			solu += i.replace("@","",1)+" "
		elif i.startswith("#"):
			solu += i.replace("#","",1)+" "
		else:
			solu += i+" "
	return solu.rstrip()
			

# end of sentences detection
#Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. What a great movie! I loved it. I loved it!!! Did you??? I did.!? Not really it was bad!"
def task56(twtText):
	return re.sub(r"(?<![A-Z][a-z])([!?.])(?=\s*[A-Z])\s*",r"\1\n",twtText)

def task7(twtText):
	
	
	


# we need to remove <\a> as a whole , not just the bracket. Your function will leave "a" which is a html tag.
# after removing it, it become english word "a", which is not correct.
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
	#total = len(sys.argv)
	#s = str(sys.argv)
	filename = sys.argv[1]
	groupID = sys.argv[2]
	output = sys.argv[3]
	filtered = []
	outf = open(sys.argv[3],"w")
	
	# tokenize everyline in the filename into this:
	#0 the polarity of the tweet (0 = negative emotion, 4 = positive emotion)
	#1 the id of the tweet (e.g., 2087)
	#2 the date of the tweet (e.g., Sat May 16 23:58:44 UTC 2009)
	#3 the query (e.g., lyx). If there is no query, then this value is NO QUERY.
	#4 the user that tweeted (e.g., robotickilldozr)
	#5-beyond the text of the tweet (e.g., Lyx is cool)
	# we now only process the text of the tweet. NOTE that twtText is a string.	
	with open(filename) as f:
		for line in f:
			tokens = line.split(",")
			twtText = ",".join(tokens[5:])
			
			
			########## Now we just have to filter twtText, by calling the helper function#####
			
			## IMPLEMENT HERE ##
			filtered.append(twtText)
		for i in filtered:
			outf.write(i+"\n")
	outf.close()
	f.close()
	


	
		


