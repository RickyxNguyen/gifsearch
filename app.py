from flask import Flask, render_template,request, send_from_directory
import os
import requests
import json
from dotenv import load_dotenv
app = Flask(__name__)

"""
The code below helps Flask load the "environment" file which contains a parameter telling the Flask server to
run in developer mode (when a change is made, the server auto reloads the changes) and also contains a parameter
that has our Tenor API key.
"""
APP_ROOT = os.path.join(os.path.dirname(__file__), './')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

api_consumer_key = os.getenv('TENOR_API_KEY')

# The code below loads the little icon that shows up at the top of the browser next to the website Title.
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

"""
The code below builds the API request URL for when a user searches for a query. It uses a Python dictionary for each
portion of the URL. After the URL is built and sent, the Tenor service returns a JSON of results which we then send
as a list inside the "gifs" variable. The render_template function then returns the website, the query, and the list
of GIFs.
"""
@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "apikey": api_consumer_key,
        "q": query,
        "limit":9
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search?", params=params)

    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None

    # print(gifs)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", query=query, gifs=gifs)

"""
The code below does the same building of the API request URL as the above function. However, this API request URL
does not require a user query since it loads the most trending GIFs. The URL is built and sent in the same way and
the render_template function returns only two variables.
"""
@app.route('/trending')
def trending():
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    params = {
        "apikey": api_consumer_key,
        "limit":9
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/trending?", params=params)

    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    return render_template("index.html",gifs=gifs)

"""
The code below does the same building of the API request URL as the above two functions. This API request URL
requires a user parameter however. The URL is built and sent in the same way and the render_template function
returns the same three variables as the first function. The difference between this and the first function is
that this uses the user query to load random GIF images related to the query instead of the most relevant images.
"""
@app.route('/random')
def random():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "apikey": api_consumer_key,
        "q": query,
        "limit":9
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/random?", params=params)

    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    return render_template("index.html", query=query ,gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
