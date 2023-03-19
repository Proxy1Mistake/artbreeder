from fake_useragent import FakeUserAgent
class headers:
    def __init__(self):
        self.headers = {'user-agent': FakeUserAgent().random}