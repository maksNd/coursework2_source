from utils import get_all_posts, get_posts_by_user, get_post_by_pk, get_comments_by_postid, search_for_posts
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def page_lent():
    all_posts = get_all_posts()
    return render_template('index.html', all_posts=all_posts)


@app.route('/post/<int:pk>')
def page_post_by_id(pk):
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
    posts = get_posts_by_user(user_name)
    return render_template('user_feed.html', posts=posts, user_name=user_name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html')


@app.errorhandler(500)
def page_server_error(error):
    return render_template('server_error.html')


@app.route('/api/posts/')
def page_posts_as_api():
    posts = get_all_posts()
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>')
def page_post_by_id_as_api(post_id)
    post = get_post_by_pk(post_id)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777)
