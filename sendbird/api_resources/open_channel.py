from sendbird import api_endpoints
from sendbird import http_methods
from sendbird.api_resources.channel import Channel


class OpenChannel(Channel):
    RESOURCE_NAME = 'open_channel'

    def list_participants(self):
        url = self.instance_url() + api_endpoints.OPEN_CHANNEL_LIST_PARTICIPANTS
        return self.request(http_methods.HTTP_METHOD_GET, url)
