from flask import Flask, request, render_template, jsonify
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    post = get_posts_all()
    return render_template('index.html', posts=post)


@app.route('/posts/<int:uid>')
def load_posts(uid):
    post = get_post_by_pk(uid)
    comment = get_comments_by_post_id(uid)
    return render_template('post.html', comment=comment, posts=post, comment_len=len(comment))


@app.route('/search/')
def search():
    search_by = request.args['s']
    if search_by:
        posts = search_for_posts(search_by)
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts, posts_len=len(posts))


@app.route('/feed/<name>')
def user_feed(name):
    user_name = get_posts_by_user(name)
    return render_template('user-feed.html', user_name=user_name)


@app.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = get_post_by_pk(uid)
    return jsonify(post)


app.run()
