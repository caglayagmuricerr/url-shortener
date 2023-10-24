from flask import Flask, request, redirect
from flask_pymongo import PyMongo
import string
import random

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://new-user:ReQ6kz0WdiFLPFkD@cluster.2grovyh.mongodb.net/URL-Shortener?retryWrites=true&w=majority'

try:
    mongo = PyMongo(app)
    print("MongoDB connection established successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Function to generate a short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

# URL shortener routes
@app.route('/')
def index():
    return 'Welcome to the URL shortener!'

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    if not original_url:
        return 'Invalid URL', 400

    # Check if the URL is already in the database
    url_mapping = mongo.db.url_mappings.find_one({'original_url': original_url})

    if url_mapping:
        short_url = url_mapping['short_url']
    else:
        # Generate a short URL
        short_url = generate_short_url()

        # Save the mapping in the database
        mongo.db.url_mappings.insert_one({'original_url': original_url, 'short_url': short_url})

    return f'Shortened URL: {request.url_root}{short_url}'

@app.route('/<short_url>')
def redirect_to_original(short_url):
    # Redirect to the original URL based on the short URL
    url_mapping = mongo.db.url_mappings.find_one({'short_url': short_url})

    if url_mapping:
        original_url = url_mapping['original_url']
        return redirect(original_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)