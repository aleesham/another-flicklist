from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Flicklist</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

add_form = """
<form action='/add' method='post'>
    <label>
        I want to add <input type='text' name='new-movie' />
        to my watchlist.
    </label>
    <input type='submit' value='Add it!'/>
</form>
"""

@app.route("/")
def index():
    header = "<h3>Edit my watchlist</h3>"
    return page_header + header + add_form + page_footer

@app.route('/add', methods = ['POST'])
def add():
    movie = request.form['new-movie']
    sentence = 'You have added <b>{}</b> to your watchlist!'.format(movie)
    return page_header + sentence + page_footer

app.run()
