from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route("/classify", methods=["GET", "POST"])
def home():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print(
        "Starting Python Flask Server For Sports Celebrity Image Classification"
    )
    util.load_saved_artifacts()
    app.run(debug=True, port=5000)
