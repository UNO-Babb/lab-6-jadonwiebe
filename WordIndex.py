#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNumber = 0
  for line in textFile:
    lineNumber = lineNumber + 1
    wordList = line.split()
    for ch in wordList:
      ch = ch.lower()
      ch = ch.replace(".", "")
      ch = ch.replace("!", "")
      ch = ch.replace("?", "")
      ch = ch.replace(",", "")
      if ch in words:
        if lineNumber not in words[ch]:
          words[ch].append(lineNumber)
      else:
        words[ch] = [lineNumber]

  for word in words:
    print(word, words[word])
  
  #print ("fish" in words) #is a word already in the dictionary?
  #words["fish"] = [2]     #add a list to the dictionary
  #print ("fish" in words) #is the word there now?
  #words["fish"].append(5) #add to an existing list
  #print(words)


if __name__ == '__main__':
  main()
