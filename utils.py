import json


def get_posts_all():
    with open('data/data.json', 'r', encoding='utf8') as file:
        date = json.load(file)
        return date


def get_posts_by_user(user_name):
    listObj = []
    json_load = get_posts_all()
    for user in json_load:
        if user_name == user['poster_name']:
            listObj.append(user)
    return listObj


def get_comments_by_post_id(post_id):
    listObj = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments_date = json.load(file)
        for comments in comments_date:
            if post_id == comments['post_id']:
                listObj.append(comments)
        return listObj


def search_for_posts(query):
    listQuer = []
    data = get_posts_all()
    for i in data:
        if query in i['content']:
            listQuer.append(i)
    return listQuer


def get_post_by_pk(pk):
    x = get_posts_all()
    get_pk = x[pk - 1]
    return get_pk

