import requests

URL_BASE = 'https://z2faulc3l0.execute-api.us-east-2.amazonaws.com/dev/'


def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # headers = {
    #    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmZjAwYWU5NDFiMTZjNGYzNDkzZDA3ZCIsImVtYWlsIjoiYXJ0dXJvLmouYS5tQG91dGxvb2suY29tIiwibmFtZSI6IkFydHVybyBKLiIsInN1cm5hbWUiOiJBbHZhIE1vbnRveWEiLCJpYXQiOjE2Nzg5NDMwOTYsImV4cCI6MTY4MTUzNTA5Nn0.tk9mJYesxPkTfproxaGt66n1Em04drg0X_SAvKFcceI'
    # }
    #r = requests.get(
    #    f'{URL_BASE}search/sandy?page=1&limit=10&&asc', headers=headers)
    print(r.status_code)
    #print(r.text)
    print(type(r.text))
    categories = r.json()
    print(r.text)
    print(type(categories))
