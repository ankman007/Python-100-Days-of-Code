from flask import Flask, render_template
import requests

BLOG_URL = 'https://api.npoint.io/eb6cd8a5d783f501ee7d'
response = requests.get(url=BLOG_URL)
post_data = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', file_name='home-bg.jpg', posts=post_data)

@app.route('/about')
def get_about():
    return render_template('about.html', file_name='about-bg.jpg')

@app.route('/contact')
def get_contact():
    return render_template('contact.html', file_name='contact-bg.jpg')

@app.route('/posts')
def get_posts():
    return render_template('index.html', file_name='post-bg.jpg', posts=post_data)

@app.route('/posts/<int:num>')
def get_post(num):
    return render_template('post.html', file_name='post-bg.jpg', posts=post_data, blog_id=num)

if __name__ == '__main__':
    app.run()

