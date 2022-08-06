from app.bp_posts.dao.tags_dao import TagsDAO
import pytest


@pytest.fixture()
def tags_dao():
    tags_dao_instance = TagsDAO()
    return tags_dao_instance


# class TestTagsDao:
#
#     # @pytest.mark.parametrize(
#     #     "test_input, expected",
#     #     [('qwe#asd', True), ('wer wer wer', False), ('', False), ('!@$%^&*', False)]
#     # )
#     def test_is_post_with_tag(self, test_input, expected):
#         result = tags_dao.is
