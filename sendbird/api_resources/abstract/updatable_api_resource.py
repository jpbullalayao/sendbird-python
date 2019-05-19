from sendbird.api_requestor import APIRequestor
from sendbird.api_resources.abstract.api_resource import APIResource
from sendbird.http_methods import HTTP_METHOD_PUT
from sendbird.util import convert_to_sendbird_object


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
        response = requestor.request(HTTP_METHOD_PUT, url, params)
        sendbird_object = convert_to_sendbird_object(response)
        return sendbird_object
