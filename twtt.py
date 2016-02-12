import sys
import re
import NLPlib
import HTMLParser
import itertools
import codecs
import io
#html tag and attribute removal
def task1(twtText):

	a = twtText.replace("/","")
	b = a.replace("\\","")
	c = b.replace("[","")
	d= c.replace("]","")
	e= d.replace("^","")
	return re.sub(r'<.*>','',e)


def task2(twtText):
	h = HTMLParser.HTMLParser()
	sol = h.unescape(twtText)
	return sol

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

	return twtText.replace("@","").replace("#","").replace("\"","")

			
def task56(twtText):
	return re.sub(r"(?<![A-Z][a-z])([!?.])(?=\s*[A-Z])\s*",r"\1\n",twtText)

def task7(twtText):
	a = re.sub( r'([a-zA-Z0-9])([,.!?;])', r'\1 \2',twtText)
	b = a.replace("'s"," 's")
	b = re.compile(r'([0-9])\s*\.\s*([0-9])').sub(r'\1\.\2',b)
	b = re.compile(r'Capt\s*\.\s*').sub(r'Capt.',b)
 	b = re.compile(r'Col\s*\.\s*').sub(r'Col.',b)
 	b = re.compile(r'Dr\s*\.\s*').sub(r'Dr.',b)
 	b = re.compile(r'Drs\s*\.\s*').sub(r'Drs.',b)
 	b = re.compile(r'Figt\s*\.\s*').sub(r'Fig.',b)
 	b = re.compile(r'Figs\s*\.\s*').sub(r'Figs.',b)
 	b = re.compile(r'Gen\s*\.\s*').sub(r'Gen.',b)
 	b = re.compile(r'Gov\s*\.\s*').sub(r'Gov.',b)
 	b = re.compile(r'HON\s*\.\s*').sub(r'HON.',b)
 	b = re.compile(r'MR\s*\.\s*').sub(r'MR.',b)
 	b = re.compile(r'MRS\s*\.\s*').sub(r'MRS.',b)
 	b = re.compile(r'Messrs\s*\.\s*').sub(r'Messrs.',b)
 	b = re.compile(r'Miss\s*\.\s*').sub(r'Miss.',b)
 	b = re.compile(r'Mmes\s*\.\s*').sub(r'Mmes.',b)
 	b = re.compile(r'Mr\s*\.\s*').sub(r'Mr.', b)
 	b = re.compile(r'Mrs\s*\.\s*').sub(r'Mrs.',b)
 	b = re.compile(r'Ref\s*\.\s*').sub(r'Ref.', b)
 	b = re.compile(r'Rep\s*\.\s*').sub(r'Rep.', b)
 	b = re.compile(r'Reps\s*\.\s*').sub(r'Reps.', b)
 	b = re.compile(r'Sen\s*\.\s*').sub(r'Sen.', b)
 	b = re.compile(r'fig\s*\.\s*').sub(r'fig.', b)
 	b = re.compile(r'figs\s*\.\s*').sub(r'figs.', b)
 	b = re.compile(r'vs\s*\.\s*').sub(r'vs.', b)
 	b = re.compile(r'Lt\s*\.\s*').sub(r'Lt.', b)
 	b = re.compile(r'e\s*\.\s*g\s*\.').sub(r'e.g.', b)
 	b = re.compile(r'i\s*\.\s*e\s*\.').sub(r'i.e.', b)	
	return b


def task8(twtText):
	solu = ""
	twtList = twtText.split("\n")
	tags = tagger.tag(twtText)
	for i in twtList:
		twtLL = i.split()
		tags = tagger.tag(twtLL)
		subsolu = ""
		for j in range(len(twtLL)):
			subsolu += twtLL[j]+"/"+tags[j]+" "
		solu += subsolu+"\n"
	return solu

def process(inF,outFile,minline,maxline):
	outf = open(outFile,'w+')
	with io.open(inF,mode='r',encoding='latin-1') as f:  
		# tokenize everyline in the filename into this:
		#0 the polarity of the tweet (0 = negative emotion, 4 = positive emotion)
		#1 the id of the tweet (e.g., 2087)
		#2 the date of the tweet (e.g., Sat May 16 23:58:44 UTC 2009)
		#3 the query (e.g., lyx). If there is no query, then this value is NO QUERY.
		#4 the user that tweeted (e.g., robotickilldozr)
		#5-beyond the text of the tweet (e.g., Lyx is cool)
		# we now only process the text of the tweet. NOTE that twtText is a string.			
		for line in itertools.islice(f,minline,maxline):
			tokens = line.split(",")
			twtText = ",".join(tokens[5:])
			mood = tokens[0]
			mood = mood[1:-1]
			twtTag = "<A="+mood+">\n"
			singleTweet = twtTag+task8(task7(task56(task4(task3(task2(task1(twtText))))))).rstrip()
			filtered.append(singleTweet.encode("latin-1"))
		for i in filtered:
			outf.write(i+"\n")
		outf.close()
		f.close()

def test(filename):
	a = []
	with io.open(filename, encoding='latin-1') as f:
		for i in itertools.islice(f,0,5500):
			a.append(i.encode("latin-1"))
	print(len(a))
	for i in a:
		print(i)
			
# computing filter function
if __name__ == "__main__":
	
	if len(sys.argv) < 4:
		print("<Filename> <groupID> <output>")
	elif len(sys.argv) == 4:	
		filename = sys.argv[1]
		groupID = sys.argv[2]
		if int(groupID) != -1:	
			class0 = (int(groupID)*5500,(int(groupID)+1)*5500-1)
			class1 = (800000+(int(groupID)*5500),800000+(int(groupID)+1)*5500-1)
			output = sys.argv[3]
			filtered = []
			tagger  = NLPlib.NLPlib()
			process(filename,output,class0[0],class0[1])
			process(filename,output,class1[0],class1[1])
		else:
			output = sys.argv[3]
			filtered = []
			tagger  = NLPlib.NLPlib()
			process(filename,output,0,360)
			


	
	


	
		


