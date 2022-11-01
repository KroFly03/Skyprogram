import pytest
from utils import *


@pytest.fixture()
def get_data():
    posts = load_data('data/posts.json')
    comments = load_data('data/comments.json')
    return posts, comments
