from sendbird import api_endpoints
from sendbird.api_resources.channel import Channel


class GroupChannel(Channel):
    RESOURCE_NAME = "group_channel"

    def list_members(self):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_LIST_MEMBERS
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def check_if_member(self, **params):
    	if not params.get('user_id'):
    		# TODO: Handle exception here
    		pass

    	url = self.instance_url() + api_endpoints.GROUP_CHANNNEL_CHECK_IF_MEMBER
    	return self.request(http_methods, url, params=params)
