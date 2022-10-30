import json
POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'


def load_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def check_user_exist(user_name):
    posts = load_data(POST_PATH)

    for post in posts:
        if post['poster_name'] == user_name.lower():
            return True

    raise ValueError('Пользователь не найден')


def check_post_exist(post_id):
    posts = load_data(POST_PATH)

    for post in posts:
        if post['pk'] == post_id:
            return True

    raise ValueError('Пост не найден')


def get_post_by_user(user_name):
    if check_user_exist(user_name):
        user_posts = []
        posts = load_data(POST_PATH)

        for post in posts:
            if post['poster_name'] == user_name.lower():
                user_posts.append(post)

        return user_posts


def get_comments_by_post_id(post_id):
    if check_post_exist(post_id):
        post_comments = []
        comments = load_data(COMMENTS_PATH)

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)

        return post_comments


def find_posts_by_key_word(key_word):
    sought_posts = []
    posts = load_data(POST_PATH)

    for post in posts:
        if key_word.lower() in post['content'].lower():
            sought_posts.append(post)

    return sought_posts


def get_post_by_pk(pk):
    posts = load_data(POST_PATH)

    for post in posts:
        if post['pk'] == pk:
            return post
