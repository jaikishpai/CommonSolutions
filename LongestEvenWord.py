#This is a solution for the problem for the longest even word in a given sentence.
def longestevenword(sentence):
  #converting the sentence into lists
  string_list = sentence.split()
  size = 0
  #iteration through each word in the list
  for word in string_list:
    #check to see if the word has even number of characters
    if len(word)%2 == 0:
      #checking if the length of the of the word
      if size <= len(word):
        size = len(word)
        even_word = word
    else:
      continue        
  # printing the longest even word in a given sentence.
  print(even_word)


## function call to test
longestevenword("This is a cat that had a puppyy")

Output: puppyy
