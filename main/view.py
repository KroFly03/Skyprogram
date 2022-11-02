from flask import Blueprint, render_template, request, redirect
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# Основная страница
@main_blueprint.route('/')
def main_page():
    posts = load_data(POST_PATH)
    bookmark_count = load_data(BOOKMARKS_PATH)
    return render_template('index.html', posts=posts, bookmark_count=len(bookmark_count))

# Вывод поста по его номеру
@main_blueprint.route('/posts/<int:post_id>')
def show_post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)

# Вывод постов по ключевому слову
@main_blueprint.route('/search')
def search_post():
    key_word = request.args.get('s')
    posts = find_posts_by_key_word(key_word)
    return render_template('search.html', posts=posts)

# Вывод постов пользователя
@main_blueprint.route('/users/<username>')
def show_user(username):
    posts = get_post_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)

# Добавление или удаление поста в закладках
@main_blueprint.route('/bookmarks/add/<int:post_id>')
def bookmark_action(post_id):
    bookmark_click(post_id)
    return redirect('/', code=302)

# Вывод всех закладок
@main_blueprint.route('/bookmarks')
def show_bookmarks():
    bookmarks = get_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@main_blueprint.route('/tag/<tag_name>')
def show_posts_by_tag(tag_name):
    posts = get_posts_by_tag(tag_name)
    return render_template('tag.html', posts=posts, tag_name=tag_name)
