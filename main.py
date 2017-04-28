from flask import Flask, request

app = Flask(__name__)

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# TODO 1
# Include another form so the user can check off a movie from their list when they've watched it.
# Name the action '/watched-it' and name it's string parameter 'watched-movie'.


# TODO 3 (Extra Credit)
# modify your form to use a dropdown (<select>) instead a
# text box (<input type="text"/>)


# TODO 2
# Create a new route called watched-it, to receive and
# handle the request from your 'watched-it' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".


@app.route("/add", methods=['POST'])
def addMovie():
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # a form for adding new movies
    add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
    """

    # build the response string
    content = page_header + edit_header + add_form + page_footer

    return content


app.run()