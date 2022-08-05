from flask import Blueprint, jsonify
from utils import get_all_posts, get_post_by_pk
from logger import get_and_set_logger
import logging

get_and_set_logger()
logger = logging.getLogger('basic')

bp_api = Blueprint('bp_api', __name__)


@bp_api.route('/api/posts/')
def page_posts_as_api():
    logger.info('request to /api/posts')
    posts = get_all_posts()
    return jsonify(posts)


@bp_api.route('/api/posts/<int:post_id>')
def page_post_by_id_as_api(post_id):
    logger.info(f'request to /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)
