import itertools
import re

global guesses
guesses = 0

# get words
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    words.append(line[:-1].lower())
  dictionary_file.close()
  return words

# find all words in dictionary
def find_words(password):
  words = get_dictionary()
  matched_words = []
  for word in words:
    global guesses
    guesses+=1
    # loop through all words to find matches
    if word in password:
      matched_words.append(word)

  return matched_words

def crack_password(password):
  password = password.lower()
  found_words = find_words(password)
  length = len(password)
  guesses = 0

  for i in range(length):
    for combination in itertools.combinations(found_words, i):

      passwordcrack = password

      for comb in combination:
        passwordcrack = passwordcrack.replace(comb, "")
        guesses+=1
      
      if passwordcrack:
        if passwordcrack.isnumeric():
            # contains numbers which is not very poggers

            solved_numbers = []
            numbers = re.findall("[0-9]+", password)
            solved = 0
            count = 0

            for index, num in enumerate(numbers):
              numbers[index] = int(num)

            while solved != len(numbers):
              if count in numbers:
                solved_numbers.append(count)
                solved+=1

              count+=1
              guesses+=1

            print(solved_numbers)
            combination = combination + tuple(solved_numbers)
            return guesses, combination  
      else: 
        return guesses, combination