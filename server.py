from flask import Flask, jsonify
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

SPOTIPY_CLIENT_ID = '46b24680194d4e7bbbf2de4e33d7a10f'
SPOTIPY_CLIENT_SECRET = '765794381aa54cea89db65cadaa9f16e'

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

@app.route('/get_new_song', methods=['GET'])
def get_new_song():
    """Fetches a random track from Spotify based on a keyword search."""
    keyword = "pop"
    results = sp.search(q=keyword, limit=50)
    track = random.choice(results['tracks']['items'])
    track_name = track['name']
    track_artist = track['artists'][0]['name']
    track_id = track['id']
    embed_url = f"https://open.spotify.com/embed/track/{track_id}"

    return jsonify({
        "track_name": track_name,
        "track_artist": track_artist,
        "embed_url": embed_url
    })

if __name__ == '__main__':
    app.run(debug=True)
