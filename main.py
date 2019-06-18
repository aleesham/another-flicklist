from flask import Flask, request, redirect
import cgi
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



# TODO: Write a function that returns the current watchlist
# (For now, this is just a hardcoded list of movies)
def get_current_watchlist():
    return ['The Princess Bride', 'The Exorcist', 'Star Wars', 'Space Balls']

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

options = ''
for movie in get_current_watchlist():
    options += '<option value="{0}">{0}</option>'.format(movie)

# TODO: Dynamically build a crossoff form using the function 
# we just wrote. (call it get_current_watchlist)
# a form for crossing off watched movies
crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(options)


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    # TODO: Validate that the movie submitted in the form
    # is actually in our current watchlist
    crossed_off_movie = request.form['crossed-off-movie']
    if crossed_off_movie in get_current_watchlist():
        crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
        confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
        content = page_header + "<p>" + confirmation + "</p>" + page_footer
        return content
    error_endpoint = "/?error='{}' is not in your Watchlist, so you can't cross it off".format(crossed_off_movie)
    error_endpoint_escaped = cgi.escape(error_endpoint)
    return redirect(error_endpoint_escaped)


@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


# TODO: if there's an error, display it. 
@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"


    error_element = ''
    error = request.args.get('error', '')
    if error:
        error_element = "<p style='color: red;'>{}</p>".format(error)


    # build the response string
    content = page_header + edit_header + add_form + crossoff_form + error_element + page_footer

    return content


app.run()



"""
http://localhost:5000/?error=%27T.he%20Bride%27%20is%20not%20in%20your%20Watchlist,%20so%20you%20can%27t%20cross%20it%20off
"""
