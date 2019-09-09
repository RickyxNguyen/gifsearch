from flask import Flask, render_template, request
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
query = 'panda'


@app.route('/')
def index():
    urls = []
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "query": query,
        "apikey": api_consumer_key
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params.get('query'), params.get('apikey'), 9))

    json_data = r.json()
    for i in range(len(json_data['results'])):
        # This is the url from json.
        url = json_data['results'][i]['media'][0]['gif']['url']
        urls.append(url)

    print(urls)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")


@app.route('/trending')
def trending():
    urls = []
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    params = {
        "apikey": api_consumer_key
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        "https://api.tenor.com/v1/trending?key=%s&limit=%s" % (params.get('apikey'), 9))

    json_data = r.json()
    for i in range(len(json_data['results'])):
        # This is the url from json.
        url = json_data['results'][i]['media'][0]['gif']['url']
        urls.append(url)
    print(urls)

    return render_template("index.html")


@app.route('/random')
def random():
    urls = []
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "query": query,
        "apikey": api_consumer_key
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        "https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (params.get('query'), params.get('apikey'), 9))

    json_data = r.json()
    for i in range(len(json_data['results'])):
        # This is the url from json.
        url = json_data['results'][i]['media'][0]['gif']['url']
        urls.append(url)

    print(urls)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
