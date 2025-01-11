from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        if request.method == 'POST':
            # Get form data from POST request
            total_sqft = request.form.get('total_sqft')
            location = request.form.get('location')
            bhk = request.form.get('bhk')
            bath = request.form.get('bath')
        else:
            # Get query parameters from GET request
            total_sqft = request.args.get('total_sqft')
            location = request.args.get('location')
            bhk = request.args.get('bhk')
            bath = request.args.get('bath')

        # Ensure that all values are present and log them
        print(f"Received data: sqft={total_sqft}, location={location}, bhk={bhk}, bath={bath}")

        # Check for missing data
        if not total_sqft or not location or not bhk or not bath:
            return jsonify({"error": "Missing data"}), 400

        # Convert types and log
        total_sqft = float(total_sqft)
        bhk = int(bhk)
        bath = int(bath)

        # Log conversion success
        print(f"Data after conversion: sqft={total_sqft}, location={location}, bhk={bhk}, bath={bath}")

        # Generate response with the estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Log estimated price
        print(f"Estimated price: {estimated_price}")

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        # Log the full exception for debugging
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()