import json
from app.constants import FILE_WITH_BOOKMARKS


class BookmarksDAO:
    data_source = FILE_WITH_BOOKMARKS

    def __init__(self, path: str = data_source):
        self.data_source = path

    def _safe_posts_to_bookmarks(self, posts: list[dict]) -> None:
        """Сохраняет посты в файл"""
        with open(self.data_source, 'w', encoding='utf-8') as file:
            json.dump(posts, file, ensure_ascii=False, indent=2)

    def get_posts_from_bookmarks(self) -> list[dict]:
        """Загружает посты из файла"""
        with open(self.data_source, encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def add_post_to_bookmarks(self, post: dict | None) -> None:
        """Добавляет посты в файл"""
        if post is None:
            return None
        posts = self.get_posts_from_bookmarks()
        posts.insert(0, post)
        self._safe_posts_to_bookmarks(posts)

    def delete_post_from_bookmarks(self, pk: int) -> None:
        """Удаляет посты из файла"""
        posts = self.get_posts_from_bookmarks()
        for post in posts:
            if post['pk'] == pk:
                posts.remove(post)
        self._safe_posts_to_bookmarks(posts)
