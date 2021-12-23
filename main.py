from flask import Flask, send_from_directory
from flask import jsonify
import glob
from flask_cors import CORS

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)


@app.route("/")
def all():
    info = {}
    for folder_name in ['midi', 'audio']:
        all_files = glob.glob(f"./static/{folder_name}/*")
        info[folder_name] = [f.replace("./static/", "") for f in all_files]
    return jsonify(info)


@app.route("/<path:path>")
def midi(path):
    return send_from_directory("./static/", path)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
