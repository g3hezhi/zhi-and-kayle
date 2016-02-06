import sys
import re

#WORDLIST KEY = featurename,  first-person pronouns
#WORLDLIST value = words in given wordlist file.
WORDLIST = {}

#add dictionary to global varibale WORDLIST, using provided wordlist file .
#For example : given First-person wordlist file, we produce output
#a = creDict("First-person","First-person","/PRP")
#{'First-person': ['I/PRP', 'ME/PRP', 'MY/PRP', 'MINE/PRP', 'WE/PRP', 'US/PRP', 'OUR/PRP', 'OURS/PRP']}
def creDict(fileName,keyName,tagName):
  wordlist = []
  with open(fileName) as f:
    for line in f:
      wordlist.append(line.upper().rstrip()+"/"+tagName)
  WORDLIST[keyName]= wordlist
  return WORDLIST

#this function put sentences from same tweet together.
#out put a list of list, each element in inner list represent a senetences in a twt.
#[[S11,S12,S13.....],[S21,S22,S23....],.....]
def readTwt(tagFile):
  twts = []
  sentences = []
  with open(tagFile) as	f:
    demarcation = f.readline()
    for line in f:
      #needs to be improve later on
      if ("<A=0>\n" == line or "<A=2>\n" == line or "<A=4>\n" == line or "<A=#>\n" == line):
        sentences.append(demarcation)
        twts.append(sentences)
        sentences = []
        demarcation = line
      sentences.append(line)
  f.close()
  return twts
        
#this function handle most of the features that involve counting number of certain 
#PoS tag in a twt.
#return a string contain all of the words with "tag"
#example: 
#a = ["stellargirl/NN I/PRP loooooooovvvvvveee/NN my/PRP$ Kindle2/NN ./."]
#tagChecker(a,"PRP")
#'I/PRP my/PRP$'
def tagChecker(twt,tag):
  strTag = ""
  for sen in twt:
    for i in sen.split():
      if re.search(".*/"+tag+"",i):
        strTag += i+" "
  return strTag.rstrip()

# using the dictionary WORDLIST and strTag we created above.
# compare the current token with our wordlist.
def tagCounter(featureName,tagName,twt):
  wordlist = WORDLIST[featureName]
  strTAG = tagChecker(twt,tagName)
  count = 0
  for i in strTAG.split():
    for j in wordlist:
      if j.upper() in i.upper():
        count += 1
  return count

def directTagCounter(twt,tag):
    count = 0
    for sen in twt:
      for i in sen.split():
        if re.search(".*/"+tag+"",i):
          count +=1
    return count  
  
#count average length of a sentence (in tokens) per tweet
def avgSentence(twt):
  sums = 0
  for senLength in twt:
    sums += len(senLength.split())
  # the -1 represent the demarcation
  return sums/(len(twt)-1)

#count the number of sentences in a twt
def numOfSentence(twt):
   # the -1 represent the demarcation
  return len(twt) - 1 

#count average length of a sentence (in character excluding punctuation tokens
def avgLenToken(twt):
  twtStr = 0
  total = 0
  for sentence in twt:
    for i in sentence.split():
      if re.search(".*/[#@.,:()]",i):
        continue
      else:
        twtStr += len(i)
        total += 1
        
  if total != 0:
    return twtStr/total
  else:
    return -1

if __name__ == "__main__":
  #a = ["stellargirl/NN I/PRP loooooooovvvvvveee/NN my/PRP$ Kindle2/NN ./. "]
  #creDict("First-person","First-person","/PRP")
  #b = tagCounter("First-person","PRP",a)
  #inputFile = sys.argv[1]
  #outputFile = open(sys.argv[2],"w")
  
  ## third argument is optional
  #MxNumTwt = sys.argv[3]
  #result = []
  
  #with open(inputFile) as f:
    #for line in f:
      #token = line.split("")
      ## after parser gerthered, write to new arff 
      #result.append(line)
    #for i in result:
      #outputFile.write(i+"\n")
  
  #INITIALLIZE DICT
  twts = readTwt("result.txt")
  print(twts)
  creDict("First-person","First-person-pronouns","PRP")
  creDict("Second-person","Second-person-pronouns","PRP")
  creDict("Third-person","Third-person-pronouns","PRP")
  creDict("Conjunct","Coordinating-conjunctions","CC")
  numFeature = []
  for i in twts:
    numFPP = tagCounter("First-person-pronouns","PRP",i)
    numSFP = tagCounter("Second-person-pronouns","PRP",i)
    numTFP = tagCounter("Third-person-pronouns","PRP",i)
    numCC = directTagCounter(i,"CC")
    numFeature.append([numFPP,numSFP,numTFP,numCC])
  print(numFeature)
  print(len(numFeature))
    