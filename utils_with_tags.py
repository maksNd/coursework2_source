def is_post_with_tag(content):
    """Проверяет пост на наличие тэга #"""
    if '#' in content:
        return True


def get_words_with_tag(content):
    """Возвращает список слов, начинающихся с тэга #"""
    content = content.replace('.', '')
    words_with_tag = []
    for word in content.split(' '):
        if len(word) > 1 and word[0] == '#':
            words_with_tag.append(word)
    return words_with_tag


def change_words_with_tag_to_link_in_content(content):
    """Заменяет слова в тексте на ссылки"""
    if is_post_with_tag(content):
        words_with_tag = get_words_with_tag(content)
        for word in words_with_tag:
            content = content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>')
    return content


def change_words_with_tag_to_link_in_all_posts(posts, key_for_change):
    """Заменяет слова во всех постах на ссылки"""
    for post in posts:
        post[key_for_change] = change_words_with_tag_to_link_in_content(post[key_for_change])
    return posts

