from sendbird import api_endpoints
from sendbird.api_resources.channel import Channel


class GroupChannel(Channel):
    RESOURCE_NAME = "group_channel"

    def list_members(self):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_LIST_MEMBERS
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def check_if_member(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_CHECK_IF_MEMBER
        # TODO: Add user_id to url
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params)

    def accept_invitation(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_ACCEPT_INVITATION
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def reject_invitation(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_REJECT_INVITATION
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def join(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_JOIN
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def leave(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_LEAVE
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def hide(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_HIDE
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)
