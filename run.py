from flask import Flask, jsonify
from main.view import main_blueprint
from utils import *


app = Flask(__name__)
app.register_blueprint(main_blueprint)


@app.route('/api/posts')
def show_posts():
    posts = load_data(POST_PATH)
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def show_post(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
