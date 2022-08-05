import json
from constants import FILE_WITH_COMMENTS, FILE_WITH_POSTS, FILE_WITH_BOOKMARKS


def get_all_posts(path=FILE_WITH_POSTS):
    """возвращает посты"""
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
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


def get_posts_by_tag_word(tag_word):
    """Возвращает посты с тэгом"""
    all_posts = get_all_posts()
    wanted_posts = []
    for post in all_posts:
        if tag_word in post['content']:
            wanted_posts.append(post)
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


def load_all_comments(path=FILE_WITH_COMMENTS):
    """возвращает все комментарии"""
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_comments_by_post_id(post_id):
    """возвращает комментарии рл post_id"""
    all_comments = load_all_comments()
    wanted_comments = []
    for comment in all_comments:
        if comment['post_id'] == post_id:
            wanted_comments.append(comment)
    return wanted_comments
