from flask import Flask, jsonify
from main.view import main_blueprint
from utils import *
import logging


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
logging.basicConfig(filename='api.log', level=logging.INFO, encoding='utf-8', format='%(asctime)s [%(levelname)s]Запрос %(message)s')


@app.route('/api/posts')
def show_posts():
    logging.info('api/posts')
    posts = load_data(POST_PATH)
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def show_post(post_id):
    logging.info(f'api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
