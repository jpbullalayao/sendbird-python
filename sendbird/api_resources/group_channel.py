from sendbird import api_endpoints
from sendbird.api_resources.channel import Channel


class GroupChannel(Channel):
    RESOURCE_NAME = "group_channel"

    def list_members(self):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_LIST_MEMBERS
        return self.request(http_methods.HTTP_METHOD_GET, url)
