import run

keys_should_be = {'content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'}


class TestApi:

    def test_api_get_posts(self):
        response = run.app.test_client().get('/api/posts')
        assert type(response.json) == list, 'Возращается не список'
        assert response.json[0].keys() == keys_should_be, 'Возращаются неверные ключи'

    def test_api_get_post(self):
        response = run.app.test_client().get('/api/posts/1')
        assert type(response.json) == dict, 'Возращается не словарь'
        assert response.json.keys() == keys_should_be, 'Возращаются неверные ключи'
