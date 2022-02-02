import random

def randomize_words(words):
  random.shuffle(words)
  result = ' '.join(words)
  print(result)

if __name__ == '__main__':
  words = input(str("Enter words: ")).split()
  randomize_words(words)
  