from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace YOUR_USER_ID with your Roblox user ID
ROBLOX_USER_ID = 'YOUR_USER_ID'

@app.route('/')
def home():
    return "Welcome to the Roblox Recent Uploads API!"

@app.route('/recent_uploads', methods=['GET'])
def get_recent_uploads():
    url = f'https://inventory.roblox.com/v1/users/{ROBLOX_USER_ID}/assets?assetType=1&limit=9'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["data"]
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
