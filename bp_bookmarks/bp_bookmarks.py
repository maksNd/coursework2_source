from flask import Blueprint, render_template, redirect
from utills_with_bookmark import add_post_to_bookmarks, get_posts_from_bookmarks, delete_post_from_bookmarks
from utils import get_post_by_pk

bp_bookmarks = Blueprint('bp_bookmarks', __name__, template_folder='templates')


@bp_bookmarks.route('/bookmarks/add/<int:pk>')
def add_post_to_bookmarks_and_redirect(pk):
    post = get_post_by_pk(pk)
    add_post_to_bookmarks(post)
    return redirect('/', code=302)


@bp_bookmarks.route('/bookmarks/')
def page_with_bookmarks():
    posts = get_posts_from_bookmarks()
    return render_template('bookmarks.html', posts=posts)


@bp_bookmarks.route('/bookmarks/remove/<int:pk>')
def delete_post_from_bookmark(pk):
    delete_post_from_bookmarks(pk)
    return redirect('/bookmarks/')
