import sys

def Analysisor(twtText):
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
  "0" 
  "Meet/VB me/PRP today/NN at/IN the/DT FEC/NN in/IN DC/NN at/IN 4/NN ./."
  Negative,
  number of VB: 1
  number of PRP: 1
  number of NN: 4
  number of IN: 1
  number of DT: 1 
  numebr of /.: 1
  '''

  









if __name == "__main__":
  inputFile = sys.argv[1]
  outputFile = open(sys.argv[2],"w")
  
  # third argument is optional
  MxNumTwt = sys.argv[3]
  result = []
  
  with open(inputFile) as f:
    for line in f:
      token = line.split(",")
      # after parser gerthered, write to new arff 
      result.append(line)
    for i in result:
      outputFile.write(i+"\n")