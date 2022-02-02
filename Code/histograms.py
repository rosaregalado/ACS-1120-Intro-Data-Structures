import random

# input = "one fish two fish red fish blue fish"
# output = {"one" -> 1, "fish" -> 4, "two" -> 1, "red" -> 1, "blue" -> 1}

def read_file(file_name):
  s = ""
  with open(file_name, 'r') as f:
    for line in f:
      s += line
    return s

# dictionary (key-value pairs)
def histogram(source_text):
  spaced_text = source_text.replace('\n', ' ')
  split_text = spaced_text.split(' ')
  output = {}
  for word in split_text:
    if word in output:
      output[word] += 1
    else:
      output[word] = 1
  return output

# def histogram2():
#   f = "source_text.txt"
#   f = open(f, 'r')

#   word_list = []

#   for l in f:
#     l = l.split()
#     for word in l:
#       word_list.append(word)

#   # sorts by alpha order
#   word_list.sort()
#   word_dictionary = {} #output dictionary

#   for word in word_list:
#     word_dictionary[word] = word_list.count(word)

#   for word in word_dictionary:
#     print((word, word_dictionary[word]))
#   print("")


# # lists in list
# def histogram3(source_text):
#   words = source_text.split(' ')
#   # print(words)
#   histogram_lists = []
#   for word in words:
#     counter = 0
#     for word2 in words:
#       if word == word2: 
#         counter += 1
#     if [word, counter] not in histogram_lists:
#       histogram_lists.append([word, counter])
#   return histogram_lists

# def unique_words(histogram):
#   return len(histogram)

# def frequency(word, histogram):
#   return histogram[word]


if __name__ == "__main__":
  text = read_file("source_text.txt")
  # print(text) 
  print(histogram(text))
  # print(histogram2(text))

