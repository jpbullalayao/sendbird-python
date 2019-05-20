from sendbird import http_methods
from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.util import convert_to_sendbird_object


class DeletableAPIResource(APIResource):
    def delete(self, api_token=None):
        requestor = APIRequestor(
            api_token
        )
        
        url = self.instance_url()
        response = requestor.request(http_methods.HTTP_METHOD_DELETE, url)
        sendbird_object = convert_to_sendbird_object(response)
        return sendbird_object

