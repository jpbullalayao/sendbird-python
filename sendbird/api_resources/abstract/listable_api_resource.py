from sendbird import api_requestor
from sendbird.http_methods import HTTP_METHOD_GET
from sendbird.api_resources.abstract.api_resource import APIResource


class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, api_token=None):
        requestor = api_requestor.APIRequestor(
            api_token
        )

        url = cls.class_url()
        return requestor.request(HTTP_METHOD_GET, url)
