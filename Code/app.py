"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, redirect, request
from dictogram import Dictogram
from markov_chain import markov_chain, markov_dict, sample
# import twitter

app = Flask(__name__)


def read_file(file_name):
  s = []
  with open(file_name, 'r') as f:
    for line in f:
      for word in line:
        s.append(word)
  return s

text = read_file('Code/corpus.txt')
# tokens = tokenize(text)
markov = markov_chain(text)

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
  output_sentence = (markov_chain(tokens))
  return output_sentence

@app.route('/tweet', methods=['POST'])
def tweet():
  status = request.form['sentence']
  twitter.tweet(status)
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)
