from app.bp_posts.dao.posts_dao import PostsDAO
import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO()
    return posts_dao_instance


post_keys_should_be = {"poster_name", "poster_avatar", "pic",
                       "content", "views_count", "likes_count", "pk"}


class TestPostsDao:

    def test_get_all_posts(self, posts_dao):
        posts = posts_dao.get_all_posts()
        assert type(posts) == list
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_get_post_by_user(self, posts_dao):
        posts = posts_dao.get_posts_by_user('leo')
        assert type(posts) == list, "Возвращается не list"
        assert len(posts) > 0, "Возвращается пустой список"
        assert posts[0]['poster_name'] == 'leo', "Возвращаются неправильные посты"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_search_for_posts(self, posts_dao):
        posts = posts_dao.search_for_posts('1')
        assert type(posts) == list, "Возвращается не list"
        assert len(posts) > 0, "Возвращается пустой список"
        assert ('1' in posts[0]['content']) == True, "Неверный поиск"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_get_post_by_pk(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Возвращается не dict"
        assert post['pk'] == 1, "Неверный поиск"
        assert set(post.keys()) == post_keys_should_be, "Неверное множество ключей"

