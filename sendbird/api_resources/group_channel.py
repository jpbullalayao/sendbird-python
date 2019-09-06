from sendbird import api_endpoints
from sendbird import http_methods
from sendbird.api_resources.channel import Channel


class GroupChannel(Channel):
    RESOURCE_NAME = "group_channel"

    def list_members(self):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_LIST_MEMBERS
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def check_if_member(self, **params):
        user_id = params.get("user_id")
        formatted_endpoint = api_endpoints.GROUP_CHANNEL_CHECK_IF_MEMBER.format(
            user_id=user_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params).is_member

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

    def unhide(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_UNHIDE
        return self.request(http_methods.HTTP_METHOD_DELETE, url, params=params)

    def reset_chat_history(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_RESET_CHAT_HISTORY
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def invite_users(self, **params):
        url = self.instance_url() + api_endpoints.GROUP_CHANNEL_INVITE_USERS
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)
