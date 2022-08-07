from app.bp_posts.dao.comments_dao import CommentsDAO
import pytest


@pytest.fixture()
def comments_dao():
    mock_path = 'tests/mock/comments_mock.json'
    comments_dao_instance = CommentsDAO(mock_path)
    return comments_dao_instance


comment_keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestCommentsDAO:

    def test_load_all_comments(self, comments_dao):
        all_comments = comments_dao.load_all_comments()
        assert type(all_comments) == list, "Возвращается не list"
        assert len(all_comments) > 0, "Возвращается пустой список"
        assert set(all_comments[0].keys()) == comment_keys_should_be, "Неверное множество ключей"

    def test_get_comments_by_post_id(self, comments_dao):
        comment = comments_dao.get_comments_by_post_id(1)
        assert type(comment) == list, "Возвращается не list"
        assert comment[0]['post_id'] == 1, "Неверный поиск"
        assert comment[0]["comment"] == "Очень здорово!"
        assert set(comment[0].keys()) == comment_keys_should_be, "Неверное множество ключей"
