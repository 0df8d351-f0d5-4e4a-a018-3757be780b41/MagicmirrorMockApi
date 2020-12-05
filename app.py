from flask import Flask
from flask import request
from flask import abort
import time
import random

app = Flask(__name__)


@app.route('/MockScoreSingleImage', methods=['POST'])
def mock_score_single_image():

    response = {
        "timestamp": int(round(time.time() * 1000)),
        "filename": request.files["image"].filename,
        "rank": random.randrange(-400, 400) / 100.0
    }

    return response


@app.route('/MockScoreSingleImageRanks', methods=['POST'])
def mock_score_single_image_ranks():

    response = {
        "timestamp": int(round(time.time() * 1000)),
        "filename": request.files["image"].filename,
        "popularity": random.randrange(-400, 400) / 100.0,
        "aesthetic": random.randrange(-400, 400) / 100.0,
        "technical": random.randrange(-400, 400) / 100.0,
        "usa": random.randrange(-400, 400) / 100.0,
        "uk": random.randrange(-400, 400) / 100.0,
        "north_europe": random.randrange(-400, 400) / 100.0,
        "south_europe": random.randrange(-400, 400) / 100.0,
        "china": random.randrange(-400, 400) / 100.0,
        "japan": random.randrange(-400, 400) / 100.0
    }

    return response


@app.route('/MockScoreMultiImage', methods=['POST'])
def mock_score_multi_image():

    print(request)

    response = {
        "timestamp": int(round(time.time() * 1000)),
        "files": []
    }

    for file in request.files:

        filedata = request.files[file]
        rank = random.randrange(-400, 400) / 100.0
        filename = filedata.filename

        item = {
            "fileid": file,
            "filename": filename,
            "rank": rank,
            "rankmap": {
                "popularity": rank,
                "aesthetic": random.randrange(-400, 400) / 100.0,
                "technical": random.randrange(-400, 400) / 100.0,
                "usa": random.randrange(-400, 400) / 100.0,
                "uk": random.randrange(-400, 400) / 100.0,
                "north_europe": random.randrange(-400, 400) / 100.0,
                "south_europe": random.randrange(-400, 400) / 100.0,
                "china": random.randrange(-400, 400) / 100.0,
                "japan": random.randrange(-400, 400) / 100.0
            }
        }
        response["files"].append(item)

    # time.sleep(3)
    # abort(500, 'server error')

    print(response)
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=8999, debug=True)
