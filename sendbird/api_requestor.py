import requests
import sendbird


class APIRequestor(object):
    def __init__(
        self,
        api_token=None,
        client=None,
        api_base=None,
    ):
        self.api_token = api_token or sendbird.api_token
        self.api_base = api_base or sendbird.api_base

    def request(self, http_method, url, params=None):
        response = self.request_raw(http_method, url, params)
        print response
        # TODO: Need to interpret response eventually into a dict
        return response.text

    def request_raw(self, http_method, url, params=None):
        abs_url = "{api_base}{url}".format(
            api_base=self.api_base,
            url=url
        )

        headers = self.request_headers()
        method_to_use = getattr(requests, http_method.lower())

        # TODO: Handle other status codes besides 200
        print headers
        print method_to_use
        return method_to_use(abs_url, headers=headers, params=params)

    def request_headers(self):
        headers = {
            "Api-Token": self.api_token,
        }
        return headers
