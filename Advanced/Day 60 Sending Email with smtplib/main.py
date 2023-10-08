from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
MY_EMAIL = 'ankitpoudel.seo007@gmail.com'
MY_PASSWORD = 'skkczghdggberkxl'
RECEIVER_EMAIL = 'ankeetpoudel6@gmail.com'

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f'Subject: { message }\n\nName: {name}\nEmail: {email}\nPhone No: {phone}'
            )
        return render_template("contact.html", message='Successfully Sent Your Message!!')
    return render_template("contact.html", message='Contact Me')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
