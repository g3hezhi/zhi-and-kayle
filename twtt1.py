import sys
import re
import NLPlib
import HTMLParser
A = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. What a great movie! I loved it. I loved it!!! Did you??? I did.!? Not really it was bad! it's"
#### write help function that only take string/list as input, and output desired processed string##

#html tag and attribute removal
def task1(twtText):
	twtList = twtText.split()
	solu =""
	for i in twtList:
		if "<" in i or ">" in i or "/" in i or "\\" in i or "[" in i or "+" in i or "]" in i or "^" in i:
			continue
		else:
			solu += i+" "
	return solu.rstrip()



def task2(twtText):
	h = HTMLParser.HTMLParser()
	sol = h.unescape(twtText)
	return sol
	## all chacter in ascii, except numbers and alphabets
	#a = twtText.replace("&gt;", ">")
	#b = a.replace("&quot;", "\"")
	#c = b.replace("&amp;", "&")
	#d = c.replace("&lt;", "<")
	#e = d.replace("&#32;","")
	#f = e.replace("&#33;","!")
	#g = f.replace("&#34;","\"")
	#h = g.replace("&#35;","#")
	#i = h.replace("&#36;","$")
	#j = i.replace("&#37;","%")
	#k = j.replace("&#38;","&")
	#l = k.replace("&#39;","\'")
	#m = l.replace("&#40;","(")
	#n = m.replace("&#41;",")")
	#o = n.replace("&#42;","*")
	#p = o.replace("&#43;","+")
	#q = p.replace("&#44;",",")
	#r = q.replace("&#45;","-")
	#s = r.replace("&#46;",".")
	#t = s.replace("&#47;","/")
	#u = t.replace("&#58;",":")
	#v = u.replace("&#59;",";")
	#w = v.replace("&#60;","<")
	#x = w.replace("&#61;","=")
	#y = x.replace("&#62;",">")
	#z = y.replace("&#63;","?")
	##loks like pushing shits together .....
	#return z	

#URL removal : www or http
def task3(twtText):
	twtList = twtText.split()
	solu = ""
	for i in twtList:
		if i.lower().startswith("www.") or i.lower().startswith("http"):
			continue
		else:
			solu += i+" "
	return solu.rstrip()
			
# @ and # removeal
def task4(twtText):
	#twtList = twtText.split()
	#solu = ""
	#for i in twtList:
		#if i.startswith("@"):
			#solu += i.replace("@","",1)+" "
		#elif i.startswith("#"):
			#solu += i.replace("#","",1)+" "
		#else:
			#solu += i+" "
	
	return twtText.replace("@","").replace("#","").replace("\"","")
			

# end of sentences detection
#Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. What a great movie! I loved it. I loved it!!! Did you??? I did.!? Not really it was bad!"
def task56(twtText):
	return re.sub(r"(?<![A-Z][a-z])([!?.])(?=\s*[A-Z])\s*",r"\1\n",twtText)

def task7(twtText):
	#return re.sub(r"(?<![A-Z][a-z])([,!?.])(?=\s*[A-Z])\s*",r"\1",twtText)
	a = re.sub( r'([a-zA-Z0-9])([,.!?;])', r'\1 \2',twtText)
	b = a.replace("'s"," 's")
	b = re.compile(r'e\s*\.\s*g\s*\.').sub(r'e.g.', b)
	b = re.compile(r'i\s*\.\s*e\s*\.').sub(r'i.e.', b)
	b = re.compile(r'Mr\s*\.\s*').sub(r'Mr.', b)
	b = re.compile(r'([0-9])\s*\.\s*([0-9])').sub(r'\1\.\2',b)
	return b


def task8(twtText):
	solu = ""
	twtList = twtText.split("\n")
	tagger  = NLPlib.NLPlib()
	tags = tagger.tag(twtText)
	for i in twtList:
		#print("my i")
		#print(i)
		twtLL = i.split()
		#print("my twtLL")
		#print(twtLL)
		tags = tagger.tag(twtLL)
		subsolu = ""
		for j in range(len(twtLL)):
			subsolu += twtLL[j]+"\\"+tags[j]+" "
		#print(subsolu)
		solu += subsolu+"\n"
	return solu
	

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
			twtTag = "<A=#>\n"
			singleTweet = twtTag+task8(task7(task56(task4(task3(task2(task1(twtText)))))))
			
			########## Now we just have to filter twtText, by calling the helper function#####
			
			## IMPLEMENT HERE ##
			filtered.append(singleTweet)
		for i in filtered:
			print(i)
			outf.write(i+"\n")
	outf.close()
	f.close()
	


	
		


