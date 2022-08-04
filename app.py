from utils import get_all_posts, get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts
from utils_with_tags import change_words_with_tag_to_link_in_content, change_words_with_tag_to_link_in_all_posts
from flask import Flask, jsonify, render_template, request
from logger import get_and_set_logger
import logging

get_and_set_logger()

logger = logging.getLogger('basic')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def page_lent():
    logger.info('request to main page')
    all_posts = get_all_posts()
    return render_template('index.html', all_posts=all_posts)


@app.route('/post/<int:pk>')
def page_post_by_id(pk):
    post = get_post_by_pk(pk)
    post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search')
def page_with_posts_by_query():
    s = request.values.get('s')
    posts = search_for_posts(s)
    for post in posts:
        post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    return render_template('search.html', posts=posts)


@app.route('/user/<user_name>')
def page_with_posts_by_user(user_name):
    posts = get_posts_by_user(user_name)
    for post in posts:
        post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    return render_template('user_feed.html', posts=posts, user_name=user_name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html')


@app.errorhandler(500)
def page_server_error(error):
    return render_template('server_error.html')


@app.route('/api/posts/')
def page_posts_as_api():
    logger.info('request to /api/posts')
    posts = get_all_posts()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def page_post_by_id_as_api(post_id):
    logger.info(f'request to /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777)
