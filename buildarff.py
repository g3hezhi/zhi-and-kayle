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

def filter(twts):
  pass
  
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
def wordListTgCounter(featureName,tagName,twt):
  wordlist = WORDLIST[featureName]
  strTAG = tagChecker(twt,tagName)
  count = 0
  for i in strTAG.split():
    for j in wordlist:
      if i.upper().replace("$","") in j.upper():
        count += 1
  return count

def directTagCounter(twt,tag):
    count = 0
    for sen in twt:
      for i in sen.split():
        if re.search(".*/"+tag+"",i):
          count +=1
    return count  

def futuretenseCounter(twt):
  count = 0
  for sen in twt:
    temp = ""
    for i in sen.split():
      temp += i+" "
      if "'LL/MD" in i.upper() or "WILL/MD" in i.upper() or "GONNA/VBG" in i.upper():
        count += 1
    if "GOING/VBG TO/TO" in temp.upper().rstrip():
      count += 1
  return count

def wordCounter(twt,pun):
  count = 0
  for sen in twt:
    for i in sen.split():
      if pun in i:
        count += 1
  return count

def removeMood(tweets):
  twt = []
  for line in tweets:
    if ("<A=0>\n" == line or "<A=2>\n" == line or "<A=4>\n" == line or "<A=#>\n" == line):
      continue
    else:
      twt.append(line)
  return twt
  
def allUpperWord(twt):
  count = 0
  for sen in twt:
    for i in sen.split():
      j = i.split("/")[0]
      if len(j) >= 2 and j == j.upper():
        count += 1
  return count
#count average length of a sentence (in tokens) per tweet
def avgSentence(twt):
  if len(twt) <= 0:
    return 0
  else:
    sums = 0
    for senLength in twt:
      sums += len(senLength.split())
    return sums/(len(twt))

#count the number of sentences in a twt
def numOfSentence(twt):
  return len(twt)

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
  #note that most slang are tagged as NN, some of them tag as NNS, for easier
  #comparison, I tag all of them as NNS in my dictionary, so
  # shm/NN in smh/NNS is true, another special cases, u/PRP considered as slang
  creDict("Slang","Modern-slang","NNS")
  numFeature = []
  for j in twts:
    i = removeMood(j)
    numFPP = wordListTgCounter("First-person-pronouns","PRP",i)
    numSFP = wordListTgCounter("Second-person-pronouns","PRP",i)
    numTFP = wordListTgCounter("Third-person-pronouns","PRP",i)
    numCC = directTagCounter(i,"CC")
    numPTV = directTagCounter(i,"VBD")
    numFTV = futuretenseCounter(i)
    numCom = wordCounter(i,",")
    numCol = wordCounter(i,":")
    numDas = wordCounter(i,"-")
    numPar = wordCounter(i,"(") + wordCounter(i,")")
    numEll = wordCounter(i,"...")
    numCommonNouns = directTagCounter(i,"NN") + directTagCounter(i,"NNS")
    numProperNouns = directTagCounter(i,"NNP") + directTagCounter(i,"NNPS")
    numAdv = directTagCounter(i,"RB") + directTagCounter(i,"RBR") + directTagCounter(i,"RBS")
    numWH = directTagCounter(i,"WDT") + directTagCounter(i,"WP") + directTagCounter(i,"WP$") + directTagCounter(i,"WRB")
    #special case : u/PRP is a slang
    numSlang = wordListTgCounter("Modern-slang","NN",i) + wordCounter(i,"u/PRP")
    numUpper = allUpperWord(i)
    avgSenLen = avgSentence(i)
    avgTokenLen = avgLenToken(i)
    numSen = numOfSentence(i)
    mood = j[-1]
    numFeature.append([numFPP,numSFP,numTFP,numCC,numPTV,numFTV,numCom,numCol,numDas,numPar,numEll,numCommonNouns,numProperNouns,numAdv,numWH,numSlang,numUpper,avgSenLen,avgTokenLen,numSen,mood])
    
  print(numFeature)
  print(len(numFeature))
  # 20 feature include the mood
  print(len(numFeature[0]))
  
  inputFile = sys.argv[1]
  outputFile = open(sys.argv[2],"w")
  write_arff = ("@RELATION twtText\n\n\n"+
  "@ATTRIBUTES 1stppronoun NUMERIC\n"+
  "@ATTRIBUTES 2ndppronoun NUMERIC\n"+
  "@ATTRIBUTES 3rdppronoun NUMERIC\n"+
  "@ATTRIBUTES co_conjunction NUMERIC\n"+
  "@ATTRIBUTES past_tenseverb NUMERIC\n"+
  "@ATTRIBUTES future_tensever NUMERIC\n"+
  "@ATTRIBUTES comma NUMERIC\n"+
  "@ATTRIBUTES colon NUMERIC\n"+  
  "@ATTRIBUTES dash NUMERIC\n"+
  "@ATTRIBUTES parenthese NUMERIC\n"+   
  "@ATTRIBUTES ellipse NUMERIC\n"+
  "@ATTRIBUTES common_noun NUMERIC\n"+
  "@ATTRIBUTES proper_noun NUMERIC\n"+ 
  "@ATTRIBUTES adverb NUMERIC\n"+
  "@ATTRIBUTES wh_word NUMERIC\n"+
  "@ATTRIBUTES acroynms NUMERIC\n"+
  "@ATTRIBUTES upper NUMERIC\n"+
  "@ATTRIBUTES avglen_sentence NUMERIC\n"+
  "@ATTRIBUTES avglen_token NUMERIC\n"+
  "@ATTRIBUTES num_sentence NUMERIC\n\n\n"+ 
  
  "@DATA\n")  
  outputFile.write(write_arff)
  for i in range(len(numFeature)):
    line =" ".join(str(x) for x in numFeature[i])
    outputFile.write(line)
    
    