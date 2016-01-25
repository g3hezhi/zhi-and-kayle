import sys

#### write help function that only take string/list as input, and output desired processed string##

#html tag and attribute removal
def task1(twtText):
	'''
	input = st = "Meet me today at the FEC in DC at 4. Wear a carnation so I know it¡¯s you. \d href=Http://bit.ly/PACattack <a href=Http://bit.ly/PACattack ?> + ^ g"
	output = 'Meet me today at the FEC in DC at 4. Wear a carnation so I know it¡¯s you. g'
	'''
	twtList = twtText.split()
	print(twtList)
	solu =""
	for i in twtList:
		if "<" in i or ">" in i or "/" in i or "\\" in i or "[" in i or "+" in i or "]" in i or "^" in i:
			continue
		else:
			solu += i+" "
	return solu.rstrip()

#convert html codes to Ascii 

def task2(twtText):
	# all chacter in ascii, except numbers and alphabets
	a = twtText.replace("&gt;", ">")
	b = a.replace("&quot;", "\"")
	c = b.replace("&amp;", "&")
	d = c.replace("&lt;", "<")
	e = d.replace("&#32;","")
	f = e.replace("&#33;","!")
	g = f.replace("&#34;","\"")
	h = g.replace("&#35;","#")
	i = h.replace("&#36;","$")
	j = i.replace("&#37;","%")
	k = j.replace("&#38;","&")
	l = k.replace("&#39;","\'")
	m = l.replace("&#40;","(")
	n = m.replace("&#41;",")")
	o = n.replace("&#42;","*")
	p = o.replace("&#43;","+")
	q = p.replace("&#44;",",")
	r = q.replace("&#45;","-")
	s = r.replace("&#46;",".")
	t = s.replace("&#47;","/")
	u = t.replace("&#58;",":")
	v = u.replace("&#59;",";")
	w = v.replace("&#60;","<")
	x = w.replace("&#61;","=")
	y = x.replace("&#62;",">")
	z = y.replace("&#63;","?")
	#loks like pushing shits together .....
	return z

#test string	
a = "one &quot; two  &amp;  three &lt; four &gt; rdm1 &#32; rdm2 &#37; rdm3 &#42;"

		

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
	return twtText.replace("#","").replace("@","")

# need to think about it.
# end of sentences detection 
#def task5

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
	


	
		


