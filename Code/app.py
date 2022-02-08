"""Main script, uses other modules to generate sentences."""
from flask import Flask
# from sample import sample, read_file, histogram
from dictogram import Dictogram

app = Flask(__name__)


def read_file(file_name):
  s = []
  with open(file_name, 'r') as f:
    for line in f:
      for word in line.split(' '):
        s.append(word)
    return s


@app.before_first_request
def before_first_request():
  """Runs only once at Flask startup"""
  # TODO: Initialize your histogram, hash table, or markov chain here.
  word_list = read_file('book.txt')
  histogram = Dictogram(word_list=word_list)
  return histogram

@app.route("/")
def home():
  """Route that returns a web page containing the generated text."""
  # return "<p>TODO: Return a word here!</p>"
  histogram = before_first_request()
  word = histogram.sample()
  return word



if __name__ == "__main__":
  app.run(debug=True)
