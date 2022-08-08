class TagsDAO:

    def _is_post_with_tag(self, content: str) -> bool:
        """Проверяет пост на наличие тэга #"""
        if '#' in content:
            return True
        return False

    def _clean_end_tag_word(self, tag_word: str) -> str:
        """Очищает слово с тэгом от символов в конце"""
        symbols_to_remove = ('.', ',', '!', '?')
        if tag_word[-1] in symbols_to_remove:
            tag_word = tag_word[:-1]
        return tag_word

    def get_first_tag_word(self, content: str) -> str:
        """Возвращает первое слово с тэгом из текста"""
        firs_tag_word = ''
        for word in content.split(' '):
            if len(word) > 1 and word[0] == '#':
                firs_tag_word = self._clean_end_tag_word(word)
                return firs_tag_word
        return firs_tag_word

    def get_list_with_tag_words(self, content: str) -> list:
        """Возвращает список слов, начинающихся с тэга #"""
        words_with_tag = []
        for word in content.split(' '):
            if len(word) > 1 and word[0] == '#':
                word = self._clean_end_tag_word(word)
                words_with_tag.append(word)
        return words_with_tag

    def change_tag_words_to_link_in_content(self, content: str) -> str:
        """Заменяет слова в тексте на ссылки"""
        if self._is_post_with_tag(content):
            words_with_tag = self.get_list_with_tag_words(content)
            for word in words_with_tag:
                content = content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>')
        return content
