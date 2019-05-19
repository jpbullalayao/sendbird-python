from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.http_methods import HTTP_METHOD_GET
from sendbird.util import convert_to_sendbird_object


class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, api_token=None):
        requestor = APIRequestor(
            api_token
        )

        url = cls.class_url()
        response = requestor.request(HTTP_METHOD_GET, url)
        sendbird_object = convert_to_sendbird_object(response)
        return sendbird_object
