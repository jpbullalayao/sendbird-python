import requests
import sendbird


class APIRequestor(object):
    def __init__(
        self,
        key=None,
        client=None,
        api_base=None,
    ):
        self.api_key = key
        self.api_base = api_base or sendbird.api_base
