from utils import get_all_posts, get_posts_by_user, search_for_posts, \
                  get_post_by_pk, load_all_comments, get_comments_by_post_id

post_keys_should_be = {"poster_name", "poster_avatar", "pic",
                  "content", "views_count", "likes_count", "pk"}

comment_keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestUtils:
    def test_get_all_posts(self):
        posts = get_all_posts()
        assert type(posts) == list
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_get_post_by_user(self):
        posts = get_posts_by_user('leo')
        assert type(posts) == list, "Возвращается не list"
        assert len(posts) > 0, "Возвращается пустой список"
        assert posts[0]['poster_name'] == 'leo', "Возвращаются неправильные посты"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_search_for_posts(self):
        posts = search_for_posts('1')
        assert type(posts) == list, "Возвращается не list"
        assert len(posts) > 0, "Возвращается пустой список"
        assert ('1' in posts[0]['content']) == True, "Неверный поиск"
        assert set(posts[0].keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_get_post_by_pk(self):
        post = get_post_by_pk(1)
        assert type(post) == dict, "Возвращается не dict"
        assert post['pk'] == 1, "Неверный поиск"
        assert set(post.keys()) == post_keys_should_be, "Неверное множество ключей"

    def test_load_all_comments(self):
        all_comments = load_all_comments()
        assert type(all_comments) == list, "Возвращается не list"
        assert len(all_comments) > 0, "Возвращается пустой список"
        assert set(all_comments[0].keys()) == comment_keys_should_be, "Неверное множество ключей"

    def test_get_comments_by_post_id(self):
        comment = get_comments_by_post_id(1)
        assert type(comment) == list, "Возвращается не list"
        assert comment[0]['post_id'] == 1, "Неверный поиск"
        assert set(comment[0].keys()) == comment_keys_should_be, "Неверное множество ключей"
