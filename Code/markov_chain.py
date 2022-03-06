from dictogram import Dictogram
import random
from random import choice
from tokenize import tokenize


def markov_dict(dictionary):
  word_list = text.split()
  markov_dict = {}
  words_range = range(len(word_list) - 2)

  for word_index in words_range:
    first_word = word_list[word_index]
    second_word = word_list[word_index + 1]
    third_word = word_list[word_index + 2]

    curr_tuple = (first_word, second_word)

    if curr_tuple in markov_dict:
      # increase count of third word
      markov_dict[curr_tuple].add_count(third_word)
    else:
      # add to dictionary
      markov_dict[curr_tuple] = Dictogram([third_word])

  return markov_dict

# output_dict = {
#     (I, like): {
#         dogs: 1,
#         cats: 1
#     },
#     (like, dogs): {
#         and: 1,
#     },
# } 

# returns a word randomly sampled by weighing it's frequency
def sample(histogram):
  # word count
  count = 0
  # dart = random number
  dart = random.random()
  for key,value in histogram.items(): 
    # increment count with each key
    count += value
    if count >= dart: 
      return key


def markov_chain(dictionary):
  # grab keys
  # dict_keys = []
  # for key, value in dictionary.items():
  #   dict_keys.append(key)
  # convert keys to list
  # dictionary = dictionary.keys()
  dict_keys = [key for key, value in dictionary.items()]
  word_list = list(dict_keys[random.randint(0, len(dict_keys) - 1)])

  for word_index in range(10):
    tuple_key = tuple((word_list[index]) for index in range(word_index, word_index + 2))
    if tuple_key in dictionary:
      word_dictogram = dictionary[tuple_key]
      next_word = sample(word_dictogram)
      word_list.append(next_word)
    else:
      break
  # return sentence
  return " ".join(word_list)

  


if __name__ == "__main__":
  with open("Code/corpus.txt", "r") as f:
    text = f.read()
    # # print(markov_chain(markov_dict(text)))
    print(markov_chain(markov_dict(text)))

    
  # text = "I like dogs and you like dogs. I like cats and you like cats"
  # print(markov_chain(markov_dict(text)))



# markov chain pseudocode sample:
# -----------------------------------------------------------------------------------------------------

# def create_markov(word_list):
#     take in a word list
#     iterate every two words (if they exist)
#
#     put both words in a tuple
#     Check if this tuple was in a dictionary,
#         if it was, increment the count for the next word (+1)
#         else: make a new entry with the value being the next word initialized to 1
#     return markov chain
# markov_chain = create_markov(word_list)

# seed the first word to be the first word of the word list (“I”)
# sentence = wordlist[0]
# “I like dogs”
# loop for until we hit our sentence length limit:
#     check if sentence[-1] is in any of the tuples[1] keys in our markov_chain,
#     and then use sample() function to choose the next word from that histogram,
#     append that word to the sentence
# return sentence
# -----------------------------------------------------------------------------------------------------
