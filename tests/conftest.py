import pytest
from utils import *


# Фикстура: загрузка данных постов и комментариев
@pytest.fixture()
def get_data():
    posts = load_data('data/posts.json')
    comments = load_data('data/comments.json')
    return posts, comments
