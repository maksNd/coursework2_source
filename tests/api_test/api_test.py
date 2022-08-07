import pytest
from app.main import app
from tests.constants_for_tests import MOCK_POSTS
# from app.bp_posts.dao.posts_dao import PostsDAO
#
#
# к сожалению не смог придумать как замокать posts_dao

mock_path = MOCK_POSTS


@pytest.fixture()
def test_client():
    app.config['DATA_SOURCE'] = mock_path
    return app.test_client()


class TestAPI:

    def test_get_all_posts_as_api(self, test_client):
        # posts_da0_instance = PostsDAO(mock_path)
        result = test_client.get('/api/posts/').json
        assert type(result) == list

    def test_get_posts_by_pk_as_api(self, test_client):
        result = test_client.get('/api/posts/1').json
        assert type(result) == dict
