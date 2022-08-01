import json
from pprint import pp

from constants import FILE_WITH_COMMENTS, FILE_WITH_POSTS, FILE_WITH_BOOKMARKS


def get_all_posts(path=FILE_WITH_POSTS):
    """возвращает посты"""
    with open(FILE_WITH_POSTS, encoding='utf-8') as file:
        return json.load(file)


def get_post_by_user(user_name):
    """
    возвращает посты определенного пользователя,
    или вызывает ошибку ValueError если у пользователя нет постов
    """
    all_posts = get_all_posts()
    wanted_posts = []
    for post in all_posts:
        if post['poster_name'].strip().lower() == user_name.strip().lower():
            wanted_posts.append(post)

    if len(wanted_posts) == 0:
        raise ValueError(f'У пользователя {user_name} еще нет постов')

    return wanted_posts


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    all_posts = get_all_posts()
    wanted_posts = []
    for post in all_posts:
        if query.strip().lower() in post['content'].strip().lower():
            wanted_posts.append(post)
    return wanted_posts


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    all_posts = get_all_posts()
    for post in all_posts:
        if post['pk'] == pk:
            return post
    return None



# pp(get_post_by_user('123'))
# pp(search_for_posts('вот'))
# pp(get_post_by_pk(20))