from flask import Flask, render_template, request

from posts_dao import PostsDAO
from comments_dao import CommentsDAO
from tags_dao import TagsDAO
from bookmark_dao import BookmarksDAO

from bp_bookmarks.bp_bookmarks import bp_bookmarks
from bp_api.bp_api import bp_api
from bp_error.bp_error import bp_error

posts_dao = PostsDAO()
comments_dao = CommentsDAO()
tags_dao = TagsDAO()
bookmark_dao = BookmarksDAO()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(bp_bookmarks, url_prefix='/bookmarks/')
app.register_blueprint(bp_api, url_prefix='/api/')

# app.register_blueprint(bp_error)


@app.route('/')
def page_lent():
    all_posts = posts_dao.get_all_posts()
    bookmarks = bookmark_dao.get_posts_from_bookmarks()
    return render_template('index.html', all_posts=all_posts, bookmarks=bookmarks)


@app.route('/post/<int:pk>')
def page_post_by_id(pk):
    post = posts_dao.get_post_by_pk(pk)
    post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    comments = comments_dao.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search/')
def page_with_posts_by_query():
    s = request.values.get('s')
    posts = posts_dao.search_for_posts(s)
    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('search.html', posts=posts)


@app.route('/users/<user_name>')
def page_with_posts_by_user(user_name):
    posts = posts_dao.get_posts_by_user(user_name)
    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('user_feed.html', posts=posts, user_name=user_name)


@app.route('/tag/<tag_word>')
def page_with_posts_by_tag(tag_word):
    posts = tags_dao.get_posts_by_tag_word(tag_word)
    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('tag.html', posts=posts, tag_word=tag_word)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html')


@app.errorhandler(500)
def page_server_error(error):
    return render_template('server_error_500.html')


@app.errorhandler(ValueError)
def page_value_error(error):
    return render_template('error_no_posts.html', message=error)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)
