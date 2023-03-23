from requests import Session
from .util import *
class artBreader:
    def __init__(self):
        self.url = 'https://www.artbreeder.com/{}'.format
        self.headers = headers().headers
        self.session = Session()

    def register(self, email: str, password: str, username: str):
        data = {
            'email': email,
            'email_pref': 'false',
            'password': password,
            'refferal': 'null',
            'username': username
        }
        req = self.session.post(url = self.url('create_user'), headers = self.headers, json = data)
        return req.text

    def login(self, email: str, password: str):
        data = {
            'email': email,
            'password': password
        }
        req = self.session.post(url = self.url('login'), headers = self.headers, json = data)
        return req.text

    def randomJsonArt(self, limit: int, models: str):
        '''
        models : anime_portraits, portraits_sg2, furries, general, landscapes_sg2_concept, buildings, paintings, sci_bio_art,
        characters, albums
        '''
        data = {"limit":limit, "offset":0, "order_by":"random", "models":[models]}
        req = self.session.post(url = self.url('images'), headers = self.headers, json = data)
        return randomJsonArt(req.json()).randomJsonArt

    def getTheCreatorImages(self, creatorId: int, limit: int):
        data = {
            "offset": 56,
            "limit": limit,
            "creator": creatorId,
            "tag_search_type": "substring",
            "models": "all",
            "tags": [],
            "tagged_by": 'null',
            "order_by": "likes"
        }
        req = self.session.post(url = self.url('beta/api/images/popular.json'), headers = self.headers, json = data)
        return getTheCreatorImages(req.json()).getTheCreatorImages()

    def getСreatorData(self, creatorName: str):
        req = self.session.get(url = self.url(f'{creatorName}/__data.json'), headers = self.headers)
        return getСreatorData(req.json()).getСreatorData

    def getImageChildren(self, key: str, limit: int):
        data = {
            "image_key": key,
            "offset": 0,
            "limit": limit
        }
        req = self.session.post(url = self.url('image_children'), headers = self.headers, json = data)
        return getImageChildren(req.json()).getImageChildren

    def getImage(self, key: str):
        req = self.session.get(url = f'https://artbreeder.b-cdn.net/imgs/{key}_small.jpeg', headers = self.headers)
        img = open(f'{key}.jpeg', 'wb')
        img.write(req.content)
        img.close()