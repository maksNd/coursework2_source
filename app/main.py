from flask import Flask

from app.bp_posts.bp_posts import bp_posts
from app.bp_bookmarks.bp_bookmarks import bp_bookmarks
from app.bp_api.bp_api import bp_api
from app.bp_error_handlers.bp_error_handlers import bp_error_handlers

app = Flask(__name__)
app.json.ensure_ascii = False

app.register_blueprint(bp_posts)
app.register_blueprint(bp_bookmarks, url_prefix='/bookmarks/')
app.register_blueprint(bp_api, url_prefix='/api/')
app.register_blueprint(bp_error_handlers)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
