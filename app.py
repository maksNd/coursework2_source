from utils import get_all_posts, get_posts_by_user, get_post_by_pk, get_comments_by_postid, search_for_posts
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def page_lent():
    all_posts = get_all_posts()
    return render_template('index.html', all_posts=all_posts)


@app.route('/post/<int:pk>')
def page_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_postid(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search')
def page_with_founded_posts():
    s = request.values.get('s')
    posts = search_for_posts(s)
    return render_template('search.html', posts=posts)


@app.route('/user/<user_name>')
def page_with_posts_by_user(user_name):
    # user_name = request.args.get('user_name')
    posts = get_posts_by_user(user_name)
    print(user_name)


if __name__ == '__main__':
    app.run(debug=True)
