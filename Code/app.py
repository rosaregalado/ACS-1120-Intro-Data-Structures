"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, redirect, request
from dictogram import Dictogram
from markov_chain import markov_chain, markov_dict, sample
# from histograms import read_file
import twitter

app = Flask(__name__)


# def read_file(file):
#   s = ''
#   with open(file, 'r') as f:
#     for line in f:
#       s += line
#     return s

def read_file(file):
  with open(file, "r") as f:
    text = f.read()
    return text


# input = "one fish two fish red fish blue fish"
# output = {"one" -> 1, "fish" -> 4, "two" -> 1, "red" -> 1, "blue" -> 1}

# markov_chain(markov_dict(text))

text = read_file('corpus.txt')
tokens = markov_dict(text)
markov = markov_chain(tokens)

# @app.before_first_request
# def before_first_request():
#   """Runs only once at Flask startup"""
#   # TODO: Initialize your histogram, hash table, or markov chain here.
#   word_list = read_file('Code/corpus.txt')
#   histogram = Dictogram(word_list=word_list)
#   return histogram

@app.route("/")
def home():
  """Route that returns a web page containing the generated text."""
  # return "<p>TODO: Return a word here!</p>"
  # sentence = "Hello"
  sentence = (markov_chain(tokens))
  return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
  status = request.form['sentence']
  print(status)
  twitter.tweet(status)
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)
