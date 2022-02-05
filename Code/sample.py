import random
from histograms import histogram

# sample_text = "one fish two fish red fish blue fish"

def read_file(file_name):
  s = ""
  with open(file_name, 'r') as f:
    for line in f:
      s += line
    return s

# the word with the most occurences will be returned more frequently
# sample_text = "one fish two fish red fish blue fish"
# "one fish fish fish fish two red blue"
# 'fish' will be returned more frequently

def sample(histogram):
  # dart = random number
  dart = random.randint(0, len(histogram) - 1)
  # initiate word count
  count = 0
  # iterate through keys in dictionary (key-value pairs)
  for key,value in histogram.items(): 
    # increment count with each key
    count += value
    # check if key occurence is greater than the dart random num
    if count >= dart: 
      # print('dart: ', (dart))
      # print('count of key: ', count)
      return key

# sample 10,000 words
def test_sample(sample):
  count = 0
  #for test number in range 10,000
  for value in histogram.values():
    count += value
  
  for key,value in histogram.items():
    probability = "{:.2f}".format((value/count)*100)
    print(f'word: {key}, probability: {probability}%\n')
    # print(f'The word {key} has appeared: {value} times')



if __name__ == '__main__':
  # sample_text = {
  #   'one': 1, 
  #   'two': 1, 
  #   'red': 1, 
  #   'blue': 1,
  #   'fish': 4
  # }  
  text = read_file("source_text.txt")
  histogram = histogram(text)
  sample(histogram)
  # test_sample(sample)
  # print(test_sample)

