import json
from constants import FILE_WITH_COMMENTS


class CommentsDAO:

    def load_all_comments(self, path: str = FILE_WITH_COMMENTS) -> list[dict]:
        """Возвращает все комментарии"""
        with open(path, encoding='utf-8') as file:
            return json.load(file)

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        """Возвращает комментарии рл post_id"""
        all_comments = self.load_all_comments()
        wanted_comments = []
        for comment in all_comments:
            if comment['post_id'] == post_id:
                wanted_comments.append(comment)
        return wanted_comments
