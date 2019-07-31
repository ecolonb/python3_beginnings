PASSWORD = '123'


def password_required(func):
    def wrapper():
        password = input('Cual es tu contrasena?')
        if password == PASSWORD:
            return func()
        else:
            print('**La contrasena no es correcta**')
            return False
    return wrapper


@password_required
def needs_password():
    print(greet_user('Edgar'))
    return True


def upper(func):
    def wrapper(*args, **kwargs):
        # name2 = args[0].upper()
        # result = func(name2)
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@upper
def greet_user(name):
    return 'Hola {} bienvenido'.format(name)


# if __name__ == '__main__':
#     needs_password()
