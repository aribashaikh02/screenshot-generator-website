from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)   
API_KEY = os.getenv("API_KEY") 
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/screenshot"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        # Placeholder: We’ll add the API call here in the next section
        return render_template('index.html', url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)