from utils import get_all_posts, get_post_by_user, get_post_by_pk
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def page_lent():
    all_posts = get_all_posts()
    return render_template('index.html', all_posts=all_posts)


app.run()
