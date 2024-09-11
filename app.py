from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Roblox Recent Uploads API!"

@app.route('/recent_uploads', methods=['GET'])
def get_recent_uploads():
    # Get the user_id parameter from the query string
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    # Call Roblox API to get recent assets for the provided user ID
    url = f'https://inventory.roblox.com/v1/users/{user_id}/assets?assetType=1&limit=9'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()["data"]
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

