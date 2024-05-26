from requests import Session
from .objects import *
from pydantic import parse_obj_as

class Artbreeder:
    _url = 'https://www.artbreeder.com/{}'.format
    _api = 'https://www.artbreeder.com/api/{}'.format

    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    @classmethod
    def __request_method(cls, method: str, url: str, data: dict = None):
        session = Session()

        if method == 'get':
            req = session.get(
                url = url,
                headers = cls.headers
            )

        else:
            req = session.post(
                url = url,
                json = data,
                headers = cls.headers)

        if req.status_code == 200:
            return req

        print(f'Error >>> {req.status_code} {req.text}')
        exit()

    @classmethod
    def register(cls, email: str, password: str, username: str) -> str:
        """
        this function is intended for registration on the site https://www.artbreeder.com/

        :param email: your email address for registration on the site
        :type email: :obj: `str`

        :param password: your password for registration on the site
        :type password: :obj: `str`

        :param username: your username for registration on the site
        :type username: :obj: `str`

        :return: response in the form of text
        """
        data = {
            'email': email,
            'redirectAfterLogin': None,
            'referral': None
        }

        cls.__request_method(
            method = 'post',
            url = cls._url('register-or-login-with-magic-link'),
            data = data
        )
        return 'check your mailbox'

    @classmethod
    def login(cls, email: str, password: str) -> str:
        """
        this function is used for authorization on the site https://www.artbreeder.com/

        :param email: the email address for your authorization on the site that you used during registration
        :type email: :obj: `str`

        :param password: the password for your authorization on the site that you used during registration
        :type password: :obj: `str`

        :return: response in the form of text
        """
        data = {
            'email': email,
            'password': password
        }

        req = cls.__request_method(
            method = 'post',
            url = cls._url('login'),
            data = data
        )

        cls.headers['cookie'] = f'connect.sid={req.cookies["connect.sid"]}'
        return req.text

    @classmethod
    def logout(cls) -> str:
        del cls.headers['cookie']
        return "You're out."

    @classmethod
    def new_username(cls, old_username, new_username, email) -> str:
        data = {
            'current_username': old_username,
            'email': email,
            'new_username': new_username
        }

        return cls.__request_method(
            method = 'post',
            url = cls._url('update_user'),
            data = data
        ).text

    @classmethod
    def new_mail(cls, email: str) -> str:
        data = {
            'email': email
        }

        return cls.__request_method(
            method = 'post',
            url = cls._url('update_email'),
            data = data
        ).text

    @classmethod
    def get_posts(cls, limit: int = 1, offset: int = 4, sort: str = 'popular_today', username: str = None):
        data = {
            'limit': limit,
            'offset': offset,
            'sort': sort,
            'username': username
        }

        req = cls.__request_method(
            method = 'post',
            url = cls._api('posts/get.json'),
            data = data
        )

        return [
            GetPosts(**_) for _ in req.json()
        ]

    @classmethod
    def get_polular_images(cls, creator: int, limit: int = 1, models: str = 'all', offset: int = 0,
                           order_by: str = 'likes', tag_search_type: str = 'substring', tags: list = []):
        data = {
            'creator': creator,
            'limit': limit,
            'models': models,
            'offset': offset,
            'order_by': order_by,
            'tag_search_type': tag_search_type,
            'tagged_by': None,
            'tags': tags
        }

        req = cls.__request_method(
            method = 'post',
            url = cls._api('images/popular.json'),
            data = data
        )

        return [
            Images(**_) for _ in req.json()
        ]

    @classmethod
    def add_comment(cls, text: str, post_key: str):
        data = {
            'imageKeys': [],
            'message': f'{text}\n\n',
            'postKey': post_key,
            'richText': [text, '\n'
            ],
            'tags': []
        }
        cls.__request_method(method = 'post',
                             url = cls._api(f'posts/{post_key}/comments/create'),
                             data = data)