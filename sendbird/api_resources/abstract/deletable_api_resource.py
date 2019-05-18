from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.http_methods import HTTP_METHOD_DELETE


class DeletableAPIResource(APIResource):
    def delete(self, api_token=None):
        requestor = APIRequestor(
            api_token
        )
        
        url = self.instance_url
        return requestor.request(HTTP_METHOD_DELETE, url)

