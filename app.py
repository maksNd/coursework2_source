from flask import Flask, render_template

from app.bp_posts.bp_posts import bp_posts
from app.bp_bookmarks.bp_bookmarks import bp_bookmarks
from app.bp_api.bp_api import bp_api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(bp_posts)
app.register_blueprint(bp_bookmarks, url_prefix='/bookmarks/')
app.register_blueprint(bp_api, url_prefix='/api/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html')


@app.errorhandler(500)
def page_server_error(error):
    return render_template('server_error_500.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
