from flask import Blueprint, render_template, request

from app.bp_posts.dao.posts_dao import PostsDAO
from app.bp_posts.dao.comments_dao import CommentsDAO
from app.bp_posts.dao.tags_dao import TagsDAO
from app.bp_bookmarks.dao.bookmark_dao import BookmarksDAO

posts_dao = PostsDAO()
comments_dao = CommentsDAO()
tags_dao = TagsDAO()
bookmark_dao = BookmarksDAO()

bp_posts = Blueprint('bp_posts', __name__, template_folder='templates')


@bp_posts.route('/')
def page_lent():
    all_posts = posts_dao.get_all_posts()
    bookmarks = bookmark_dao.get_posts_from_bookmarks()
    return render_template('index.html', all_posts=all_posts, bookmarks=bookmarks)


@bp_posts.route('/post/<int:pk>')
def page_post_by_id(pk):
    post = posts_dao.get_post_by_pk(pk)
    if post is None:
        message = f'Такого поста не существует'
        return render_template('no_posts.html', message=message)

    post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    comments = comments_dao.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@bp_posts.route('/search/')
def page_with_posts_by_query():
    s = request.values.get('s')
    if s is None:
        return 'Nothing to search. Error 404', 404
    posts = posts_dao.search_for_posts(s)
    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('search.html', posts=posts)


@bp_posts.route('/users/<user_name>')
def page_with_posts_by_user(user_name):
    posts = posts_dao.get_posts_by_user(user_name)
    if posts is None:
        message = f'У пользователя {user_name} еще нет постов'
        return render_template('no_posts.html', message=message)

    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('user_feed.html', posts=posts, user_name=user_name)


@bp_posts.route('/tag/<tag_word>')
def page_with_posts_by_tag(tag_word):
    posts = posts_dao.get_posts_by_tag_word(tag_word)
    for post in posts:
        post['tag'] = tags_dao.get_first_tag_word(post['content'])
        post['content'] = tags_dao.change_tag_words_to_link_in_content(post['content'])
    return render_template('tag.html', posts=posts, tag_word=tag_word)
