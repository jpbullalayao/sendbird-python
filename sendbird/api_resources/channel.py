from sendbird import api_endpoints
from sendbird import http_methods
from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updatable_api_resource import UpdatableAPIResource  # NOQA


class Channel(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource
):
    FIELD_PK = "channel_url"

    def instance_url(self):
        pk = self.get(Channel.FIELD_PK)

        base = self.class_url()
        return "{base}/{pk}".format(
            base=base,
            pk=pk
        )

    def freeze(self, freeze=False):
        url = self.instance_url() + api_endpoints.CHANNEL_FREEZE
        params = {
            'freeze': freeze,
        }
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def ban_user(self, **params):
        url = self.instance_url() + api_endpoints.CHANNEL_BAN_USER
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)


    def unban_user(self, **params):
        banned_user_id = params.get('banned_user_id')
        formatted_endpoint = api_endpoints.CHANNEL_UNBAN_USER.format(
            banned_user_id=banned_user_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_DELETE, url, params=params)

    def update_ban(self, **params):
        banned_user_id = params.get('banned_user_id')
        formatted_endpoint = api_endpoints.CHANNEL_UPDATE_BAN.format(
            banned_user_id=banned_user_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def list_banned_users(self, **params):
        url = self.instance_url() + api_endpoints.CHANNEL_LIST_BANNED_USERS
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params)

    def view_ban(self, **params):
        banned_user_id = params.get('banned_user_id')
        formatted_endpoint = api_endpoints.CHANNEL_VIEW_BAN.format(
            banned_user_id=banned_user_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params)

    def mute_user(self, **params):
        url = self.instance_url() + api_endpoints.CHANNEL_MUTE_USER
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)

    def unmute_user(self, **params):
        muted_user_id = params.get('muted_user_id')
        formatted_endpoint = api_endpoints.CHANNEL_UNMUTE_USER.format(
            muted_user_id=muted_user_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_DELETE, url, params=params)

