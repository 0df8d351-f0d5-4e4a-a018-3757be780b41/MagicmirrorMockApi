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
        "rank": random.randrange(40, 80) / 100.0
    }

    return response


@app.route('/MockScoreSingleImageRanks', methods=['POST'])
def mock_score_single_image_ranks():
    response = {
        "timestamp": int(round(time.time() * 1000)),
        "filename": request.files["image"].filename,
        "popularity": random.randrange(40, 80) / 100.0,
        "aesthetic": random.randrange(40, 80) / 100.0,
        "technical": random.randrange(40, 80) / 100.0,
        "usa": random.randrange(40, 80) / 100.0,
        "uk": random.randrange(40, 80) / 100.0,
        "north_europe": random.randrange(40, 80) / 100.0,
        "south_europe": random.randrange(40, 80) / 100.0,
        "china": random.randrange(40, 80) / 100.0,
        "japan": random.randrange(40, 80) / 100.0
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
        rank = random.randrange(40, 80) / 100.0
        filename = filedata.filename

        item = {
            "fileid": file,
            "filename": filename,
            "rank": rank,
            "rankmap": {
                "popularity": rank,
                "aesthetic": random.randrange(40, 80) / 100.0,
                "technical": random.randrange(40, 80) / 100.0,
                "usa": random.randrange(40, 80) / 100.0,
                "uk": random.randrange(40, 80) / 100.0,
                "north_europe": random.randrange(40, 80) / 100.0,
                "south_europe": random.randrange(40, 80) / 100.0,
                "china": random.randrange(40, 80) / 100.0,
                "japan": random.randrange(40, 80) / 100.0
            }
        }
        response["files"].append(item)

    # time.sleep(3)
    # abort(500, 'server error')

    print(response)
    return response


@app.route('/MockScoreMultiImageTest', methods=['POST'])
def mock_score_multi_image_test():
    print(request)

    response = {
        "timestamp": int(round(time.time() * 1000)),
        "files": []
    }

    i = 0

    for file in request.files:
        i = i + 1
        filedata = request.files[file]
        rank = 0.1 * i
        filename = filedata.filename

        item = {
            "fileid": file,
            "filename": filename,
            "rank": rank,
            "rankmap": {
                "popularity": rank,
                "aesthetic": 0.2 * i,
                "technical": 0.3 * i,
                "usa": 0.4 * i,
                "uk": 0.5 * i,
                "north_europe": 0.6 * i,
                "south_europe": 0.7 * i,
                "china": 0.8 * i,
                "japan": 0.9 * i
            }
        }
        response["files"].append(item)

    # time.sleep(3)
    # abort(500, 'server error')

    print(response)
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=8999, debug=True)
