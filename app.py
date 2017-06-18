import os
import time

from flask import Flask, request, jsonify, redirect

from download_images import download_image
from label_image import get_predictions

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return redirect('https://github.com/BenMusch/honhaas#hotdog-or-not-hotdog-as-as-service')

@app.route('/is_hotdog', methods=['POST'])
def is_hotdog():
    image_url = request.args.get('image')
    image_location = os.path.join('tmp', "download_%s" % int(time.time()))
    image_location = download_image(image_url, image_location)
    if image_location:
        try:
            predictions = get_predictions(image_location)
            is_hotdog = make_prediction(predictions)
            os.remove(image_location)
            return jsonify(is_hotdog=is_hotdog, scores=predictions)
        except Exception as e:
            print(str(e))
            return jsonify({ 'error': 'Error processing image' }), 500
    else:
        return jsonify({ 'error': 'Couldn\'t download image' }), 500


def make_prediction(predictions):
    return predictions[0][0] == 'hotdogs' and predictions[0][1] >= 0.8 \
            and predictions[0][1] - predictions[1][1] > 0.2


if __name__ == '__main__':
    app.run()
