from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import utils

app = Flask(__name__)
CORS(app)


@app.route("/recommend", methods=["POST"])
def get_recommended_songs():
    data = request.get_json()

    if "songs" not in data:
        return jsonify({"error": "No 'songs' key found in the request."}), 400

    songs = data["songs"]

    if not isinstance(songs, list):
        return jsonify({"error": "'songs' must be a list of song IDs."}), 400

    recommended_songs = utils.recommend_songs(songs)

    return jsonify({"recommended_songs": recommended_songs})


if __name__ == "__main__":
    app.run(debug=False)
