import json
from app.constants import FILE_WITH_POSTS


class PostsDAO:
    data_source = FILE_WITH_POSTS

    def __init__(self, path: str = data_source):
        self.data_source = path

    def get_all_posts(self) -> list[dict]:
        """Возвращает все посты"""
        with open(self.data_source, encoding='utf-8') as file:
            return json.load(file)

    def get_posts_by_user(self, user_name: str) -> list[dict] | None:
        """
        Возвращает посты определенного пользователя
        или None, если постов не найдено
        """
        all_posts = self.get_all_posts()
        wanted_posts = []
        for post in all_posts:
            if post['poster_name'].strip().lower() == user_name.strip().lower():
                wanted_posts.append(post)
        if len(wanted_posts) == 0:
            return None
        return wanted_posts

    def search_for_posts(self, query: str | None) -> list[dict] | None:
        """Возвращает список постов по ключевому слову"""
        if query is None:
            return None
        all_posts = self.get_all_posts()
        wanted_posts = []
        for post in all_posts:
            if query.strip().lower() in post['content'].strip().lower():
                wanted_posts.append(post)
        return wanted_posts

    def get_post_by_pk(self, pk: int) -> dict | None:
        """Возвращает один пост по его идентификатору"""
        all_posts = self.get_all_posts()
        for post in all_posts:
            if post['pk'] == pk:
                return post
        return None

    def get_posts_by_tag_word(self, tag_word: str) -> list:
        """Возвращает посты с тэгом"""
        all_posts = self.get_all_posts()
        wanted_posts = []
        for post in all_posts:
            if '#' + tag_word in post['content']:
                wanted_posts.append(post)
        return wanted_posts
