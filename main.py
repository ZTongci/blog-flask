from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)
blog_post = Post()


@app.route('/')
def home():
    blog_post.get_total_blog()
    total_blog = blog_post.total_blog
    return render_template("index.html", total_blog=total_blog)

@app.route('/post/<id>')
def post(id):
    id = int(id)
    blog_post.get_total_blog()
    total_blog = blog_post.total_blog
    return render_template("post.html", id=id, total_blog=total_blog)



if __name__ == "__main__":
    app.run(debug=True)
