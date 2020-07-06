from flask import Flask, render_template, request, redirect
from search import search_for_letter

app = Flask(__name__)

@app.route('/')
def hello() -> '302': # can't name this function as redirect cause the next line will call this redirect function instead of the one from flask
  return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
  return render_template('entry.html', the_title = 'Welcome to Search for Web')

@app.route('/results', methods = ['POST'])
def do_search():
  phrase = request.form['phrase']
  letters = request.form['letters']
  result = str(search_for_letter(phrase, letters))
  return render_template('results.html', the_title = 'Here Are Your Results', the_phrase = phrase, the_letters = letters, the_results = result)


if __name__ == '__main__':
  app.run(debug=True)