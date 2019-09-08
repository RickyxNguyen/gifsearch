from flask import Flask, render_template, request
import requests
import json
import urllib.request,urllib.parse,urllib.error

app = Flask(__name__)

# set the apikey and limit
api_key = "IPZD64OZGMYV"  # test value

# our test search
query = "panda"

# continue a similar pattern until the user makes a selection or starts a new search.


@app.route('/')
def index():
    urls=[]
    """Return homepage."""
    # TODO: Extract query term from url
    # query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "query": query,
        "apikey": api_key
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params.get('query'), params.get('apikey'), 10))

    json_data = r.json()
    for i in range(len(json_data['results'])):
        url = json_data['results'][i]['media'][0]['gif']['url'] #This is the url from json.
        urls.append(url)
        urllib.request.urlretrieve(url, str(i)+'.gif') #Downloads the gif file.
    print(urls)


        # load the GIFs using the urls for the smaller GIF sizes

    # else:
    #     data = None

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
