from flask import Blueprint, render_template, redirect
from app.bp_posts.dao.posts_dao import PostsDAO
from app.bp_bookmarks.dao.bookmark_dao import BookmarksDAO

posts_dao = PostsDAO()
bookmark_dao = BookmarksDAO()

bp_bookmarks = Blueprint('bp_bookmarks', __name__, template_folder='templates')


@bp_bookmarks.route('/add/<int:pk>')
def add_post_to_bookmarks_and_redirect(pk):
    post = posts_dao.get_post_by_pk(pk)
    if post is None:
        return 'No such post to add. Error 404', 404
    bookmark_dao.add_post_to_bookmarks(post)
    return redirect('/', code=302)


@bp_bookmarks.route('/')
def page_with_bookmarks():
    posts = bookmark_dao.get_posts_from_bookmarks()
    return render_template('bookmarks.html', posts=posts)


@bp_bookmarks.route('/remove/<int:pk>')
def delete_post_from_bookmark(pk):
    bookmark_dao.delete_post_from_bookmarks(pk)
    return redirect('/bookmarks/')
