import requests


class Post:
    def __init__(self):
        self.total_blog = "Post Body"

    def get_total_blog(self):
        post_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(post_url)
        self.total_blog = response.json()

