from flask import Blueprint, jsonify
from app.bp_posts.dao.posts_dao import PostsDAO
from app.logger import get_and_set_logger
import logging

get_and_set_logger()
logger = logging.getLogger('basic')

posts_dao = PostsDAO()

bp_api = Blueprint('bp_api', __name__)


@bp_api.route('/posts/')
def get_all_posts_as_api():
    logger.info('request to /api/posts')
    posts = posts_dao.get_all_posts()
    return jsonify(posts)


@bp_api.route('/posts/<int:post_id>')
def get_post_by_id_as_api(post_id):
    logger.info(f'request to /api/posts/{post_id}')
    post = posts_dao.get_post_by_pk(post_id)
    return jsonify(post)
