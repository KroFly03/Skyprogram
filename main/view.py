from flask import Blueprint, render_template, request, jsonify
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts = load_data(POST_PATH)
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:post_id>')
def show_post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search')
def search_post():
    key_word = request.args.get('s')
    posts = find_posts_by_key_word(key_word)
    return render_template('search.html', posts=posts)


@main_blueprint.route('/users/<username>')
def show_user(username):
    posts = get_post_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)
