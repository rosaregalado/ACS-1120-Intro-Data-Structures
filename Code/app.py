"""Main script, uses other modules to generate sentences."""
from flask import Flask
# from sample import sample, read_file, histogram
from dictogram import Dictogram

app = Flask(__name__)

histogram = None


def read_file(file_name):
  s = ""
  with open(file_name, 'r') as f:
    for line in f:
      s += line
    return s

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    text = read_file("source_text.txt")
    histogram = Dictogram(text=text)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # return "<p>TODO: Return a word here!</p>"
    word = histogram.sample()
    return word


if __name__ == "__main__":
    app.run(debug=True)
