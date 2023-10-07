import requests
from flask import Flask, render_template

BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(BLOG_URL)
    data = response.json()
    return render_template("index.html", posts=data)

@app.route('/post/<int:num>')
def get_post(num):
    response = requests.get(BLOG_URL)
    data = response.json()
    post = next((post for post in data if post['id'] == num), None)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
