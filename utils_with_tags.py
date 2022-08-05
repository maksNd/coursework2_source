from utils import get_all_posts


def is_post_with_tag(content: str) -> bool:
    """Проверяет пост на наличие тэга #"""
    if '#' in content:
        return True


def clean_tag_ward(tag_word: str) -> str:
    """Очищает слово с тэгом от символов в конце"""
    symbols_to_remove = ('.', ',', '!', '?')
    if tag_word[-1] in symbols_to_remove:
        tag_word = tag_word[:-1]
    return tag_word


def get_first_tag_word(content: str) -> str:
    """Возвращает первое слово с тэгом из текста"""
    firs_tag_word = ''
    for word in content.split(' '):
        if len(word) > 1 and word[0] == '#':
            firs_tag_word = clean_tag_ward(word)
            return firs_tag_word
    return firs_tag_word


def get_list_with_tag_words(content: str) -> list:
    """Возвращает список слов, начинающихся с тэга #"""
    words_with_tag = []
    for word in content.split(' '):
        if len(word) > 1 and word[0] == '#':
            word = clean_tag_ward(word)
            words_with_tag.append(word)
    return words_with_tag


def change_words_with_tag_to_link_in_content(content: str) -> str:
    """Заменяет слова в тексте на ссылки"""
    if is_post_with_tag(content):
        words_with_tag = get_list_with_tag_words(content)
        for word in words_with_tag:
            content = content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>')
    return content


def change_tag_words_to_link_in_all_posts_and_add_first_tag_word(posts: list[dict]) -> list[dict]:
    """Заменяет слова во всех постах на ссылки"""
    for post in posts:
        post['tag'] = get_first_tag_word(post['content'])
        post[post['content']] = change_words_with_tag_to_link_in_content(post['content'])
    return posts


def get_posts_by_tag_word(tag_word: str) -> list[dict]:
    """Возвращает посты с тэгом"""
    all_posts = get_all_posts()
    wanted_posts = []
    for post in all_posts:
        if '#' + tag_word in post['content']:
            wanted_posts.append(post)
    return wanted_posts
