from requests import Session
from .objects import *
from fake_useragent import FakeUserAgent
class Data:
    _headers = {
        'user-agent': FakeUserAgent().random
    }
    _session = Session()
    _url = 'https://www.artbreeder.com/{}'.format

class Artbreeder(Data):
    @classmethod
    def register(cls, email: str, password: str, username: str) -> int | str:
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
        _data = {
            'email': email,
            'email_pref': 'false',
            'password': password,
            'refferal': 'null',
            'username': username
        }
        _req = cls._session.post(url = cls._url('create_user'), headers = cls._headers, json = _data)
        if _req.status_code != 200: return _req.status_code
        else: return _req.text

    @classmethod
    def login(cls, email: str, password: str) -> int | str:
        """
        this function is used for authorization on the site https://www.artbreeder.com/

        :param email: the email address for your authorization on the site that you used during registration
        :type email: :obj: `str`

        :param password: the password for your authorization on the site that you used during registration
        :type password: :obj: `str`

        :return: response in the form of text
        """
        _data = {
            'email': email,
            'password': password
        }
        _req = cls._session.post(url = cls.url('login'), headers = cls._headers, json = _data)
        if _req.status_code != 200: return _req.status_code
        else: return _req.text

    @classmethod
    def random_json_art(cls, limit: int, models: str) -> int | ObjectRandomJsonArt:
        """
        this function is designed to get random art in json format

        :param limit: the maximum number of received art
        :type limit: :obj: `int`

        :param models: select the models you want to receive. Models : anime_portraits, portraits_sg2, furries, general, landscapes_sg2_concept, buildings, paintings, sci_bio_art, characters, albums
        :type models: :obj: `str`

        :return: random art in ObjectRandomJsonArt or int
        """
        _data = {"limit": limit, "offset": 0, "order_by": "random", "models": [models]}
        _req = cls._session.post(url = cls._url('images'), headers = cls._headers, json = _data)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectRandomJsonArt(data = _req.json()).object_random_json_art

    @classmethod
    def get_the_creator_images(cls, creator_id: int, limit: int) -> int | ObjectGetTheCreatorImages:
        """
        this function is used to get the works of a certain user

        :param creator_id: id of the user whose work you want to get
        :type creator_id: :obj: `int`

        :param limit: maximum number of user's works received
        :type limit: :obj: `int`

        :return: user's work in json format
        """
        _data = {
            "offset": 56,
            "limit": limit,
            "creator": creatorId,
            "tag_search_type": "substring",
            "models": "all",
            "tags": [],
            "tagged_by": 'null',
            "order_by": "likes"
        }
        _req = cls._session.post(url = cls._url('beta/api/images/popular.json'), headers = cls._headers, json = _data)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectGetTheCreatorImages(data = _req.json()).object_get_the_creator_images

    @classmethod
    def get_creator_data(cls, creator_name: str) -> int | ObjectGetCreatorData:
        """
        This function is designed to get user data

        :param creator_name: the name of the user whose data you want to get
        :type creator_name: :obj: `str`

        :return: user data in json format
        """
        _req = self.session.get(url = cls._url(f'{creator_name}/__data.json'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectGetCreatorData(data = _req.json()).object_get_creator_data

    @classmethod
    def get_image_children(cls, key: str, limit: int) -> int | ObjectGetImageChildren:
        """
        this function is designed to get images of children

        :param key: the key to the image
        :type key: :obj: `str`

        :param limit: Maximum number of images received children
        :type limit: :obj: `int`

        :return: images in json format
        """
        _data = {
            "image_key": key,
            "offset": 0,
            "limit": limit
        }
        _req = cls._session.post(url = cls._url('image_children'), headers = cls._headers, json = _data)
        return ObjectGetImageChildren(data = _req.json()).object_get_image_children

    @classmethod
    def get_image(cls, key: str) -> int | bytes:
        """
        this function is designed to save images

        :param key: the key to the image
        :type key: :obj: `str`

        :return: image
        """
        _req = cls._session.get(url = f'https://artbreeder.b-cdn.net/imgs/{key}_small.jpeg', headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else:
            _img = open(f'{key}.jpeg', 'wb')
            _img.write(_req.content)
            _img.close()