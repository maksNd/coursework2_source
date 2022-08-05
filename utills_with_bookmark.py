import json
from constants import FILE_WITH_BOOKMARKS


def get_posts_from_bookmarks(file_with_bookmarks: str = FILE_WITH_BOOKMARKS) -> list[dict]:
    """Загружает посты из файла"""
    with open(file_with_bookmarks, encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def send_posts_to_bookmarks(posts: list, file_with_bookmarks: str = FILE_WITH_BOOKMARKS) -> None:
    """Сохраняет посты в файл"""
    with open(file_with_bookmarks, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=2)


def add_post_to_bookmarks(post: dict) -> None:
    """Добавляет посты в файл"""
    posts = get_posts_from_bookmarks()
    posts.insert(0, post)
    send_posts_to_bookmarks(posts)


def delete_post_from_bookmarks(pk: int) -> None:
    """Удаляет посты из файла"""
    posts = get_posts_from_bookmarks()
    for post in posts:
        if post['pk'] == pk:
            posts.remove(post)
    send_posts_to_bookmarks(posts)
