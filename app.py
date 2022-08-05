from utils import get_all_posts, get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts
from utils_with_tags import change_words_with_tag_to_link_in_content, get_first_tag_word, get_posts_by_tag_word
from utills_with_bookmark import add_post_to_bookmarks, get_posts_from_bookmarks, delete_post_from_bookmarks
from flask import Flask, render_template, request
from logger import get_and_set_logger
import logging
from bp_bookmarks.bp_bookmarks import bp_bookmarks
from bp_api.bp_api import bp_api

# get_and_set_logger()

# logger = logging.getLogger('basic')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(bp_bookmarks)
app.register_blueprint(bp_api)


@app.route('/')
def page_lent():
    all_posts = get_all_posts()
    bookmarks = get_posts_from_bookmarks()
    return render_template('index.html', all_posts=all_posts, bookmarks=bookmarks)


@app.route('/post/<int:pk>')
def page_post_by_id(pk):
    post = get_post_by_pk(pk)
    post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search/')
def page_with_posts_by_query():
    s = request.values.get('s')
    posts = search_for_posts(s)
    for post in posts:
        post['tag'] = get_first_tag_word(post['content'])
        post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    return render_template('search.html', posts=posts)


@app.route('/users/<user_name>')
def page_with_posts_by_user(user_name):
    posts = get_posts_by_user(user_name)
    for post in posts:
        post['tag'] = get_first_tag_word(post['content'])
        post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    return render_template('user_feed.html', posts=posts, user_name=user_name)


@app.route('/tag/<tag_word>')
def page_with_posts_by_tag(tag_word):
    posts = get_posts_by_tag_word(tag_word)
    for post in posts:
        post['tag'] = get_first_tag_word(post['content'])
        post['content'] = change_words_with_tag_to_link_in_content(post['content'])
    return render_template('tag.html', posts=posts, tag_word=tag_word)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html')


@app.errorhandler(500)
def page_server_error(error):
    return render_template('server_error_500.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)
