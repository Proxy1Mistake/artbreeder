from requests import Session
from .objects import *
from fake_useragent import FakeUserAgent
class artbreeder:
    def __init__(self, proxies : dict = None):
        self.headers = {'user-agent': FakeUserAgent().random}
        self.proxies = proxies
        self.session = Session()
        self.url = 'https://www.artbreeder.com/{}'.format

    def register(self, email: str, password: str, username: str):
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
        self.data = {
            'email': email,
            'email_pref': 'false',
            'password': password,
            'refferal': 'null',
            'username': username
        }
        req = self.session.post(url = self.url('create_user'), headers = self.headers, json = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return req.text

    def login(self, email: str, password: str):
        """
        this function is used for authorization on the site https://www.artbreeder.com/

        :param email: the email address for your authorization on the site that you used during registration
        :type email: :obj: `str`

        :param password: the password for your authorization on the site that you used during registration
        :type password: :obj: `str`

        :return: response in the form of text
        """
        self.data = {
            'email': email,
            'password': password
        }
        req = self.session.post(url = self.url('login'), headers = self.headers, json = data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return req.text

    def random_json_art(self, limit: int, models: str):
        """
        this function is designed to get random art in json format

        :param limit: the maximum number of received art
        :type limit: :obj: `int`

        :param models: select the models you want to receive. Models : anime_portraits, portraits_sg2, furries, general, landscapes_sg2_concept, buildings, paintings, sci_bio_art, characters, albums
        :type models: :obj: `str`

        :return: random art in json format
        """
        self.data = {"limit": limit, "offset": 0, "order_by": "random", "models": [models]}
        req = self.session.post(url = self.url('images'), headers = self.headers, json = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_random_json_art(data = req.json()).obj_random_json_art

    def get_the_creator_images(self, creator_id: int, limit: int):
        """
        this function is used to get the works of a certain user

        :param creator_id: id of the user whose work you want to get
        :type creator_id: :obj: `int`

        :param limit: maximum number of user's works received
        :type limit: :obj: `int`

        :return: user's work in json format
        """
        self.data = {
            "offset": 56,
            "limit": limit,
            "creator": creatorId,
            "tag_search_type": "substring",
            "models": "all",
            "tags": [],
            "tagged_by": 'null',
            "order_by": "likes"
        }
        req = self.session.post(url = self.url('beta/api/images/popular.json'), headers = self.headers, json = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_get_the_creator_images(data = req.json()).obj_get_the_creator_images

    def get_creator_data(self, creator_name: str):
        """
        This function is designed to get user data

        :param creator_name: the name of the user whose data you want to get
        :type creator_name: :obj: `str`

        :return: user data in json format
        """
        req = self.session.get(url = self.url(f'{creatorName}/__data.json'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_get_creator_data(data = req.json()).obj_get_creator_data

    def get_image_children(self, key: str, limit: int):
        """
        this function is designed to get images of children

        :param key: the key to the image
        :type key: :obj: `str`

        :param limit: Maximum number of images received children
        :type limit: :obj: `int`

        :return: images in json format
        """
        self.data = {
            "image_key": key,
            "offset": 0,
            "limit": limit
        }
        req = self.session.post(url = self.url('image_children'), headers = self.headers, json = self.data, proxies = self.proxies)
        return obj_get_image_children(data = req.json()).obj_get_image_children

    def get_image(self, key: str):
        """
        this function is designed to save images

        :param key: the key to the image
        :type key: :obj: `str`

        :return: image
        """
        req = self.session.get(url = f'https://artbreeder.b-cdn.net/imgs/{key}_small.jpeg', headers = self.headers, proxies = self.proxies)
        img = open(f'{key}.jpeg', 'wb')
        img.write(req.content)
        img.close()