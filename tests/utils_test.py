import conftest
from utils import *


class TestUtils:

    def test_load_data(self):
        data = load_data(POST_PATH)
        assert len(data) != 0, 'Ошибка загрузки файла'

    def test_get_post_by_user(self, get_data):
        data = get_post_by_user('leo')
        assert get_data[0][0] in data, 'Ошибка получение пользователя по имени'

    def test_get_comments_by_post_id(self, get_data):
        data = get_comments_by_post_id(1)
        assert get_data[1][0] in data, 'Ошибка получения комментариев к посту'

    def test_find_posts_by_key_word(self, get_data):
        data = find_posts_by_key_word('Очень')
        assert get_data[0][6] in data, 'Ошибка поиска постов по ключевому слову'

    def test_get_post_by_pk(self, get_data):
        post = get_post_by_pk(1)
        assert get_data[0][0] == post, 'Ошибка получения поста по номеру'
