import random

def dictionary_words():
  words_list = []
  output = ""
  # actual amount of words: 235886
  total_words = 20 
  open_file = open('/usr/share/dict/words')
  words = open_file.readlines()
  # generate random number (of words)
  for i in range(total_words):
    random_number = random.randint(0, len(words)-1)
    words_list.append(words[random_number])

  for i in words_list:
    output += i
  print(output)

if __name__ == "__main__":
  dictionary_words()