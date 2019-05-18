from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.http_methods import HTTP_METHOD_POST


class CreateableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        api_token=None,
        **params
    ):
        requestor = APIRequestor(
            api_token
        )

        url = cls.class_url()
        return requestor.request(HTTP_METHOD_POST, url, params)
