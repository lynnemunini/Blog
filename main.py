from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

posts = requests.get("https://api.npoint.io/9260e848de41c3dd6999").json()
all_posts = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
