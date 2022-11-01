from flask import Blueprint, jsonify
import logging
from utils import *

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint .route('/api/posts')
def show_posts():
    logging.info('api/posts')
    posts = load_data(POST_PATH)
    return jsonify(posts)


@api_blueprint .route('/api/posts/<int:post_id>')
def show_post(post_id):
    logging.info(f'api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)
