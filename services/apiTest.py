import requests as requests
import sys


def get_posts():
    try:
        urlBlog = "https://blog.envioclick.com/wp-json/wp/v2/posts?_embed"
        r = requests.get(urlBlog)
        r = r.json()
        responseData = {"ok": True, "data": r}
        return responseData
    except requests.exceptions.RequestException as e:
        print('ConnectionError Error description -->>')
        print(dir(sys.exc_info()))
        print(sys.exc_info()[0])
        print(sys.exc_info())
    except:
        print(sys.exc_info()[0])
        print('Other Error')
    return {}
