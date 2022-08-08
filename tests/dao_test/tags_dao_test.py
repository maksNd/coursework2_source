from app.bp_posts.dao.tags_dao import TagsDAO
import pytest


@pytest.fixture()
def tags_dao():
    tags_dao_instance = TagsDAO()
    return tags_dao_instance


class TestTagsDao:

    @pytest.mark.parametrize(
        "test_input, expected",
        [('qwe#asd', True), ('wer wer', False), ('', False), ('!@$%^&*', False)]
    )
    def test_is_post_with_tag(self, tags_dao, test_input, expected):
        assert tags_dao._is_post_with_tag(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [('#dog!', '#dog'), ('#cat.', '#cat'), ('ocean,', 'ocean'), ('water?', 'water'), ('food', 'food')]
    )
    def test_clean_end_tag_word(self, tags_dao, test_input, expected):
        assert tags_dao._clean_end_tag_word(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [('alpha #bravo charlie #delta', '#bravo'), ('alpha bravo charlie delta', ''), ('', '')]
    )
    def test_get_first_tag_word(self, tags_dao, test_input, expected):
        assert tags_dao.get_first_tag_word(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [('alpha #bravo. charlie #delta!', ['#bravo', '#delta']),
         ('alpha #bravo charlie #delta', ['#bravo', '#delta']),
         ('alpha bravo charlie delta', []), ('', [])]
    )
    def test_get_list_with_tag_words(self, tags_dao, test_input, expected):
        assert tags_dao.get_list_with_tag_words(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            ('alpha bravo charlie delta', 'alpha bravo charlie delta'),
            ('alpha #bravo charlie #delta',
             'alpha <a href="/tag/bravo">#bravo</a> charlie <a href="/tag/delta">#delta</a>'),
            ('#kot #kotofeich', '<a href="/tag/kot">#kot</a> <a href="/tag/kot">#kot</a>ofeich')
        ]
    )
    def test_change_tag_words_to_link_in_content(self, tags_dao, test_input, expected):
        assert tags_dao.change_tag_words_to_link_in_content(test_input) == expected
