from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.http_methods import HTTP_METHOD_PUT


class UpdatableAPIResource(APIResource):
    def update(
    	self, 
    	api_token=None, 
    	**params
    ):
    	requestor = APIRequestor(
    		api_token
    	)

    	url = self.instance_url()
        return requestor.request(HTTP_METHOD_PUT, url, params)
