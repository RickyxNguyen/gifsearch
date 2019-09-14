from flask import Flask, render_template,request
import os
import requests
import json
from dotenv import load_dotenv
app = Flask(__name__)

# refers to application_top
APP_ROOT = os.path.join(os.path.dirname(__file__), './')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

api_consumer_key = os.getenv('TENOR_API_KEY')

# continue a similar pattern until the user makes a selection or starts a new search.

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "query": query,
        "apikey": api_consumer_key,
        "link":'https://api.tenor.com/v1/',
        "lmt":9
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        f"{params['link']}search?q={params['query']}&key={params['apikey']}&limit={params['lmt']}")

    if r.status_code ==200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None

    # print(gifs)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", query=query, gifs=gifs)


@app.route('/trending')
def trending():
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    params = {
        "apikey": api_consumer_key,
        "link":'https://api.tenor.com/v1/',
        "lmt":9


    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        f"{params.get('link')}trending?key={params['apikey']}&limit={params['lmt']}")
    if r.status_code ==200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    return render_template("index.html",gifs=gifs)


@app.route('/random')
def random():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "query": query,
        "apikey": api_consumer_key,
        "link":'https://api.tenor.com/v1/',
        "lmt":9
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        f"{params['link']}random?q={params['query']}&key={params['apikey']}&limit={params['lmt']}")

    if r.status_code ==200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    return render_template("index.html", query=query ,gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
