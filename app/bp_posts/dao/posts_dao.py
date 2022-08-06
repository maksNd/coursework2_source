import json
from constants import FILE_WITH_POSTS


class PostsDAO:

    def get_all_posts(self, path: str = FILE_WITH_POSTS) -> list[dict]:
        """Возвращает посты"""
        with open(path, encoding='utf-8') as file:
            return json.load(file)

    def get_posts_by_user(self, user_name: str) -> list[dict]:
        """
        Возвращает посты определенного пользователя,
        или вызывает ошибку ValueError если у пользователя нет постов
        """
        all_posts = self.get_all_posts()
        wanted_posts = []
        for post in all_posts:
            if post['poster_name'].strip().lower() == user_name.strip().lower():
                wanted_posts.append(post)
        if len(wanted_posts) == 0:
            raise ValueError(f'У пользователя {user_name} еще нет постов')
        return wanted_posts

    def search_for_posts(self, query: str) -> list[dict]:
        """Возвращает список постов по ключевому слову"""
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
