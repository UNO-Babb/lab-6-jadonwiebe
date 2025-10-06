#WordCount.py
#Name:Jadon Wiebe
#Date:10/05
#Assignment:Word Count

def main():
  filename = input("Enter a file name: ")
  #gettysberg.txt or fish.txt
  textFile = open(filename, 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    print(line)
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      for ch in w:
        letterCount = letterCount + 1

  print("Lines: ", lineCount)
  print("Words: ", wordCount)
  print("Letters: ", letterCount)
  

if __name__ == '__main__':
  main()
