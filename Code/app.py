"""Main script, uses other modules to generate sentences."""
from flask import Flask
from sample import sample, read_file, histogram

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    text = read_file("source_text.txt")
    word = histogram(text)
    return sample(word)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # return "<p>TODO: Return a word here!</p>"
    get_word = before_first_request()
    return get_word


if __name__ == "__main__":
    app.run(debug=True)
