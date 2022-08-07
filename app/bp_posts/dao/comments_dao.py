import json
from app.constants import FILE_WITH_COMMENTS


class CommentsDAO:
    data_source = FILE_WITH_COMMENTS

    def __init__(self, path: str = data_source):
        self.data_source = path

    def load_all_comments(self) -> list[dict]:
        """Возвращает все комментарии"""
        with open(self.data_source, encoding='utf-8') as file:
            return json.load(file)

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        """Возвращает комментарии по post_id"""
        all_comments = self.load_all_comments()
        wanted_comments = []
        for comment in all_comments:
            if comment['post_id'] == post_id:
                wanted_comments.append(comment)
        return wanted_comments
