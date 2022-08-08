from tests.constants_for_tests import MOCK_BOOKMARKS
import json

import pytest
from app.bp_bookmarks.dao.bookmark_dao import BookmarksDAO

mock_path = MOCK_BOOKMARKS


@pytest.fixture()
def bookmarks_dao():
    bookmarks_dao_instance = BookmarksDAO(mock_path)
    return bookmarks_dao_instance


post_keys_should_be = {"poster_name", "poster_avatar", "pic",
                       "content", "views_count", "likes_count", "pk"}


class TestBookmarksDAO:

    test_input = {'pk': 1000}

    def _get_data_from_mock_file(self, path: str = mock_path):
        with open(path, encoding='utf-8') as file:
            result = json.load(file)
            return result

    def _clean_mock_file(self, path: str = mock_path):
        with open(path, 'w') as file:
            json.dump([], file)

    def _write_test_data_to_mock_file(self, path: str = mock_path):
        with open(path, 'w') as file:
            json.dump([self.test_input], file)

    def test_get_posts_from_bookmark(self, bookmarks_dao):
        self._write_test_data_to_mock_file()
        posts = bookmarks_dao.get_posts_from_bookmarks()
        assert type(posts) == list
        assert len(posts) > 0

    def test_safe_posts_to_bookmarks(self, bookmarks_dao):
        bookmarks_dao._safe_posts_to_bookmarks([{'pk': 'test_message_from_safe_posts'}])
        result = self._get_data_from_mock_file()
        assert {'pk': 'test_message_from_safe_posts'} in result

    def test_add_post_to_bookmarks(self, bookmarks_dao):
        bookmarks_dao.add_post_to_bookmarks({'pk': 'test_message_from_add_post'})
        result = self._get_data_from_mock_file()
        assert {'pk': 'test_message_from_add_post'} in result
        self._clean_mock_file()

        assert bookmarks_dao.add_post_to_bookmarks(None) is None
        result = self._get_data_from_mock_file()
        assert len(result) == 0
        self._clean_mock_file()


    def test_delete_post_from_bookmarks(self, bookmarks_dao):
        self._write_test_data_to_mock_file()
        bookmarks_dao.delete_post_from_bookmarks(1000)
        result = self._get_data_from_mock_file()
        assert self.test_input not in result
        self._clean_mock_file()
