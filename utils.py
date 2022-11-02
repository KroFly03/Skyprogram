import json
POST_PATH = 'data/posts.json'
COMMENTS_PATH = 'data/comments.json'
BOOKMARKS_PATH = 'data/bookmarks.json'


def load_data(path):
    """Загрузка данных из json-файла"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def check_user_exist(user_name):
    """Проверка на существование пользователя"""
    posts = load_data(POST_PATH)

    for post in posts:
        if post['poster_name'] == user_name.lower():
            return True

    raise ValueError('Пользователь не найден')


def check_post_exist(post_id):
    """Проверка на существование поста"""
    posts = load_data(POST_PATH)

    for post in posts:
        if post['pk'] == post_id:
            return True

    raise ValueError('Пост не найден')


def get_hashtags(post):
    """Преобразование слов с хештегами в ссылки"""
    if '#' in post['content']:
        words = post['content'].split(' ')
        for index, word in enumerate(words):
            if word.startswith('#'):
                words[index] = f'<a href="/tag/{word[1:]}">{word}</a>'

        post['content'] = ' '.join(words)

    return post


def get_post_by_user(user_name):
    """Получение поста по имени пользователя"""
    if check_user_exist(user_name):
        user_posts = []
        posts = load_data(POST_PATH)

        for post in posts:
            if post['poster_name'] == user_name.lower():
                user_posts.append(post)

        return user_posts


def get_comments_by_post_id(post_id):
    """Получение комментариев к посту"""
    if check_post_exist(post_id):
        post_comments = []
        comments = load_data(COMMENTS_PATH)

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)

        return post_comments


def find_posts_by_key_word(key_word):
    """Поиск по ключевому слову"""
    sought_posts = []
    posts = load_data(POST_PATH)

    for post in posts:
        if key_word.lower() in post['content'].lower():
            sought_posts.append(post)

    return sought_posts


def get_post_by_pk(pk):
    """Получение поста по номеру"""
    posts = load_data(POST_PATH)

    for post in posts:
        if post['pk'] == pk:
            return get_hashtags(post)


def save_bookmark_to_json(bookmarks, path):
    """Сохранение пользовательских закладок"""
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False)


def delete_bookmark(user_bookmark, bookmarks):
    """Удаление закладки"""
    for index, bookmark in enumerate(bookmarks):
        if bookmark == user_bookmark:
            del bookmarks[index]
            break

    save_bookmark_to_json(bookmarks, BOOKMARKS_PATH)


def add_bookmark(user_bookmark, bookmarks):
    """Добавление закладки"""
    bookmarks.append(user_bookmark)
    save_bookmark_to_json(bookmarks, BOOKMARKS_PATH)


def bookmark_click(user_bookmark):
    """Определение статуса закладки(удаление или добавление)"""
    bookmarks = load_data(BOOKMARKS_PATH)
    if user_bookmark in bookmarks:
        delete_bookmark(user_bookmark, bookmarks)
    else:
        add_bookmark(user_bookmark, bookmarks)


def get_bookmarks():
    """Получение списка закладок"""
    user_bookmark = []
    posts = load_data(POST_PATH)
    bookmarks = load_data(BOOKMARKS_PATH)
    for post in posts:
        if post['pk'] in bookmarks:
            user_bookmark.append(post)

    return user_bookmark


def get_posts_by_tag(tag_name):
    """Получение списка постов по тегу"""
    tag_posts = []
    posts = load_data(POST_PATH)
    tag = '#' + tag_name

    for post in posts:
        if tag in post['content']:
            tag_posts.append(post)

    return tag_posts
