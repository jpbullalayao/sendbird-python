import requests
import sendbird

from sendbird.sendbird_response import SendbirdResponse


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
        rbody = self.request_raw(http_method, url, params)
        resp = self.interpret_response(rbody)
        return resp

    def request_raw(self, http_method, url, params=None):
        if url.startswith("/"):
            url = url[1:]  # Removes slash

        abs_url = "{api_base}{url}".format(
            api_base=self.api_base,
            url=url
        )
        headers = self.request_headers()
        method_to_use = getattr(requests, http_method.lower())

        # TODO: Handle other status codes besides 200
        return method_to_use(abs_url, headers=headers, json=params)

    def request_headers(self):
        headers = {
            "Api-Token": self.api_token,
            "Content-Type": "application/json, charset=utf8",
        }
        return headers

    def interpret_response(self, rbody):
        resp = SendbirdResponse(rbody.text)
        return resp
