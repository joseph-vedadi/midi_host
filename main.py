from flask import Flask, send_from_directory
from flask import jsonify
import glob
from flask_cors import CORS

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)


@app.route("/")
def all():
    all_midi = glob.glob("./static/midi/*")
    midi_files = [midi.replace("./static/midi/", "") for midi in all_midi]
    return jsonify(midi_files)


@app.route("/<path:path>")
def midi(path):
    return send_from_directory("./static/midi/", path)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
