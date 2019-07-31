from decorators.session import needs_password
from services.apiTest import get_posts

if __name__ == '__main__':
    print('hello')
    isLogged = needs_password()
    print('Logged: ' + str(isLogged))

    if(isLogged):
        postsResponse = get_posts()
        print('Keys: ' + str(dict.keys(postsResponse)))
        postsFormated = []
        for post in postsResponse.get("data", []):
            postsFormated.append({"id": post.get('id', 0)})
        print(postsFormated)
    else:
        print('Log out')
