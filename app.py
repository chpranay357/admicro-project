from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    data = response.json()
    if 'items' not in data:
        print("Response JSON:", data)
    books = data.get('items', [])
    return render_template('results.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
