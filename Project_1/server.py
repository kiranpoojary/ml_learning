from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)
#app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/loadLocations", methods=["GET"])
def getLocNames():
    response = jsonify({
        'locations': util.getLocNames()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/get", methods=["POST"])
def getPrice():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.getPrice(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Server Started......")
    util.loadArtifacts()
    app.run(debug=True)
