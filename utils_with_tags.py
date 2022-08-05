def is_post_with_tag(content):
    """Проверяет пост на наличие тэга #"""
    if '#' in content:
        return True


def clean_tag_ward(tag_word):
    """Очищает слово с тэгом от символов в конце"""
    symbols_to_remove = ('.', ',', '!', '?')
    if tag_word[-1] in symbols_to_remove:
        tag_word = tag_word[:-1]
    return tag_word


def get_list_with_tag_words(content):
    """Возвращает список слов, начинающихся с тэга #"""
    content = content.replace('.', '')
    words_with_tag = []
    for word in content.split(' '):
        if len(word) > 1 and word[0] == '#':
            word = clean_tag_ward(word)
            words_with_tag.append(word)
    return words_with_tag


def change_words_with_tag_to_link_in_content(content):
    """Заменяет слова в тексте на ссылки"""
    if is_post_with_tag(content):
        words_with_tag = get_list_with_tag_words(content)
        for word in words_with_tag:
            content = content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>')
    return content


def change_words_with_tag_to_link_in_all_posts(posts, key_for_change):
    """Заменяет слова во всех постах на ссылки"""
    for post in posts:
        post[key_for_change] = change_words_with_tag_to_link_in_content(post[key_for_change])
    return posts
