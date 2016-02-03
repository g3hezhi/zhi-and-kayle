import sys
import re

#this function put sentences from same tweet togethe.
#out put a list of list, each inner list represent a senetences in a twt.
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
def tagCounter(twt,tag):
  count = 0
  for sen in twt:
    for i in sen.split():
    #NEED TO CHANGE THIS \\ to /
      if re.search(".*\\"+tag+"",i):
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

#def test(twt):
  #twtStr = ""
  #for i in twt.split():
    #if re.search(".*\@|.*\.",i):
      #continue
    #else:
      #twtStr += i
  #return twtStr
def extractor(twtText):
  ''' 
  Gathering Features from train.twt 
  
  Feathures List:
  Counts:
  1. First person pronouns            
  2. Second person pronouns
  3. Third person pronouns
  4. Coordinating conjunctions       /CC
  5. Past-tense verbs                /VBD
  6. Future-tense verbs
  7. Commas                          /.
  8. Colons and semi-colons          /: and /;
  9. Dashes                          /-
  10. Parentheses                    /( /)
  11. Ellipses                       /...
  12. Common nouns
  13. Proper nouns                    /NNP /NNPS
  14. Adverbs                        /RB
  15. wh-words                       /WRB
  16. Modern slang acroynms
  17. Words all in upper case (at least 2 letters long)
  
  18. Average length of sentences (in tokens)
  19. Average length of tokens, excluding punctuation tokens (in characters) 
  20. Number of sentences
  
  Example:
  
  a ="Meet/VB me/PRP today/NN at/IN the/DT FEC/NN in/IN DC/NN at/IN 4/NN ./."
  Negative,
  number of VB: 1
  number of PRP: 1
  number of NN: 4
  number of IN: 1
  number of DT: 1 
  numebr of /.: 1
  '''
  '''
  dict = {
    "first person pronoun":x,
    "Second person pronouns":a,
    "Third person pronouns":b,
    "Coordinating conjunctions":c,
    "Past-tense verbs":d,
    "Future-tense verbs":e,
    "Commas":f,
    "Colons and semi-colons":g,
    "Dashes":h,
    "Parentheses":i,
    "Ellipses":j,
    "Common nouns":k,
    "Proper nouns":l,
    "Adverbs":m,
    "wh-words":n,
    "Modern slang acroynms":o,
    "Words all in upper case":p,
    "Average length of sentences":q,
    "Average length of tokens":r,
    "Number of sentences":s,
}
  print dict
  
'''
  

  count_vbd = 0
  count_cc = 0
  count_coma = 0
  count_colon = 0
  count_dash = 0
  count_parenthese = 0
  count_ellipse = 0
  count_pnoun = 0
  count_adverb = 0
  count_whword = 0
  for i in twtText.split():
    
    if re.search(".*/VBD",i):
      count_vbd +=1
    elif re.search(".*/NN",i):
      count_cc +=1
    elif re.search(".*/[,.]",i):
      count_coma +=1
    elif re.search(".*/[:;]",i):
      count_colon +=1
    elif re.search(".*/-",i):
      count_dash +=1 
      
    elif re.search(".*/[(){}\[\]]",i):
      count_parenthese +=1
    elif re.search(".*\.\.\.",i):
      count_ellipse +=1 
      
    
    
  print(count_vbd,count_cc,count_coma,count_colon,count_dash, count_parenthese, count_ellipse)
  '''test = "/VBD /CC /, /. /: /; /- /[ /) /{ /( /} /..."'''  
    








if __name__ == "__main__":
  inputFile = sys.argv[1]
  outputFile = open(sys.argv[2],"w")
  
  # third argument is optional
  MxNumTwt = sys.argv[3]
  result = []
  
  with open(inputFile) as f:
    for line in f:
      token = line.split("")
      # after parser gerthered, write to new arff 
      result.append(line)
    for i in result:
      outputFile.write(i+"\n")