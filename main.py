import os
from dotenv import find_dotenv, load_dotenv
import urllib.parse
import requests
from flask import Flask, redirect, request, jsonify, session, render_template
from datetime import *

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = 'this-is-a-secret-key'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = "http://localhost:5000/callback"

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com/v1/"

# SETTING THE HOME PAGE

@app.route('/')
def index():
    return render_template('index.html')

# REDIRECTING THE USER TO SPOTIFY'S LOGIN PAGE

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-top-read'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True # logins everytime rather than keeping the user logged in (for debugging purposes)
    }

    auth_url = f'{AUTH_URL}?{urllib.parse.urlencode(params)}'

    return redirect(auth_url) # this will redirect the user to the specific url provided

# GETTING THE ACCESS TOKEN

@app.route('/callback')
def callback():
    if 'error' in request.args: # gets all the params for a url
        return jsonify({'error': request.args['error']})

    # suppose spotify does not return an error and instead returns a 'code' parameter which contains a string that needs to be sent back as a request to get the access token
    # here, the login is successful, but we encounter a logical error

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(url=TOKEN_URL, data=req_body)
        token_info = response.json()

        # session stores the info in a temporary directory in the server till the user logs out

        session['access_token'] = token_info['access_token'] # request to spotify api
        session['refresh_token'] = token_info['refresh_token'] # what we use to refresh the access token once it expires
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in'] # the number of seconds that the access token is valid (usually 3600, 1 day)
            # this timestamp code lets us know exactly when the token expires rather than when it expires since it was generated since yu cant keep track of that

        return redirect('/artists/long_term')

# GETTING THE TOP ARTISTS FOR LONG TERM PERIOD

@app.route('/artists/long_term')
def get_artists_long():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/artists?limit=25&time_range=long_term', headers=headers)
    artists = response.json()

    artists_name = []

    for item in artists['items']:
        artists_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['images'][1]['url'],
            'name': item['name']
        })


    return render_template('artists_page.html', artists=artists_name)

# GETTING THE TOP ARTISTS FOR MEDIUM TERM PERIOD

@app.route('/artists/medium_term')
def get_artists_medium():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/artists?limit=25&time_range=medium_term', headers=headers)
    artists = response.json()

    artists_name = []

    for item in artists['items']:
        artists_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['images'][1]['url'],
            'name': item['name']
        })


    return render_template('artists_page.html', artists=artists_name)

# GETTING THE TOP ARTISTS FOR SHORT TERM PERIOD

@app.route('/artists/short_term')
def get_artists_short():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/artists?limit=25&time_range=short_term', headers=headers)
    artists = response.json()

    artists_name = []

    for item in artists['items']:
        artists_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['images'][1]['url'],
            'name': item['name']
        })


    return render_template('artists_page.html', artists=artists_name)

# GETTING THE TOP TRACKS FOR LONG TERM PERIOD

@app.route('/tracks/long_term')
def get_tracks_long():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/tracks?limit=25&time_range=long_term', headers=headers)
    tracks = response.json()

    tracks_name = []

    for item in tracks['items']:
        tracks_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['album']['images'][1]['url'],
            'artist_name': ", ".join(artist['name'] for artist in item['artists']),
            'name': item['name'],
            'album': item['album']['name'],
            'id': item['id']
        })

    return render_template('tracks_page.html', tracks=tracks_name)

# GETTING THE TOP TRACKS FOR MEDIUM TERM PERIOD

@app.route('/tracks/medium_term')
def get_tracks_medium():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/tracks?limit=25&time_range=medium_term', headers=headers)
    tracks = response.json()

    tracks_name = []

    for item in tracks['items']:
        tracks_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['album']['images'][1]['url'],
            'artist_name': ", ".join(artist['name'] for artist in item['artists']),
            'name': item['name'],
            'album': item['album']['name'],
            'id': item['id']
        })

    return render_template('tracks_page.html', tracks=tracks_name)

# GETTING THE TOP TRACKS FOR SHORT TERM PERIOD

@app.route('/tracks/short_term')
def get_tracks_short():
    if 'access_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')

    headers = {
        'Authorization': f'Bearer {session['access_token']}'
    }

    response = requests.get(API_BASE_URL + 'me/top/tracks?limit=25&time_range=short_term', headers=headers)
    tracks = response.json()

    tracks_name = []

    for item in tracks['items']:
        tracks_name.append({
            'url': item['external_urls']['spotify'],
            'image': item['album']['images'][1]['url'],
            'artist_name': ", ".join(artist['name'] for artist in item['artists']),
            'name': item['name'],
            'album': item['album']['name'],
            'id': item['id']
        })

    return render_template('tracks_page.html', tracks=tracks_name)

# GETTING THE REFRESH TOKEN ONCE THE ACCESS TOKEN EXPIRES

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')

    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'authorization_code',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(url=TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/artists/long_term')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)