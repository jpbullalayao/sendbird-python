from sendbird import api_endpoints 
from sendbird import http_methods
from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updatable_api_resource import UpdatableAPIResource  # NOQA
from sendbird.api_resources.constants import unread_count_preferences


class User(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdatableAPIResource
):
    RESOURCE_NAME = "user"

    FIELD_PK = "user_id"
    FIELD_PROFILE_URL = "profile_url"
    DEFAULT_PROFILE_URL = ""

    @classmethod
    def create(
        cls,
        api_token=None,
        **params
    ):
        profile_url = params.get(
            cls.FIELD_PROFILE_URL, cls.DEFAULT_PROFILE_URL)
        params[cls.FIELD_PROFILE_URL] = profile_url
        return super(User, cls).create(api_token=api_token, **params)

    def instance_url(self):
        pk = self.get(User.FIELD_PK)

        base = self.class_url()
        return "{base}/{pk}".format(
            base=base,
            pk=pk
        )

    def list_group_channels(self):
        url = self.instance_url() + api_endpoints.USER_MY_GROUP_CHANNELS
        return self.request(http_methods.HTTP_METHOD_GET, url)
        
    def unread_message_count(self):
        url = self.instance_url() + api_endpoints.USER_UNREAD_MESSAGE_COUNT
        return self.request(http_methods.HTTP_METHOD_GET, url).get('unread_count')

    def unread_item_count(self, params=None):
        url = self.instance_url() + api_endpoints.USER_UNREAD_ITEM_COUNT
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params)

    def mark_all_messages_as_read(self, params=None):
        url = self.instance_url() + api_endpoints.USER_MARK_AS_READ_ALL
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def block(self, **params):
        url = self.instance_url() + api_endpoints.USER_BLOCK
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)

    def list_blocked_users(self, **params):
        url = self.instance_url() + api_endpoints.USER_LIST_BLOCKED_USERS
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params)

    def unblock(self, target_id=None):
        formatted_endpoint = api_endpoints.USER_UNBLOCK.format(
            target_id=target_id
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_DELETE, url)

    def add_device_token(self, **params):
        formatted_endpoint = api_endpoints.USER_ADD_DEVICE_TOKEN.format(
            token_type=params.get('token_type')
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)

    def list_device_tokens(self, token_type=None):
        formatted_endpoint = api_endpoints.USER_LIST_DEVICE_TOKENS.format(
            token_type=token_type
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def remove_device_token(self, **params):
        formatted_endpoint = api_endpoints.USER_REMOVE_DEVICE_TOKEN.format(
            token_type=params.get('token_type'),
            token=params.get('token')
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_DELETE, url)

    def remove_all_device_tokens(self):
        url = self.instance_url() + api_endpoints.USER_REMOVE_ALL_DEVICE_TOKENS
        return self.request(http_methods.HTTP_METHOD_DELETE, url)

    @classmethod
    def view_device_token_owner(cls, **params):
        formatted_endpoint = api_endpoints.USER_VIEW_DEVICE_TOKEN_OWNER.format(
            token_type=params.get('token_type'),
            token=params.get('token')
        )

        resp = User.static_request(http_methods.HTTP_METHOD_GET, formatted_endpoint)
        if hasattr(resp, 'error'):
            return resp
        return resp[0].user_id

    @classmethod
    def remove_device_token_from_owner(self, **params):
        formatted_endpoint = api_endpoints.USER_REMOVE_DEVICE_TOKEN_FROM_OWNER.format(
            token_type=params.get('token_type'),
            token=params.get('token')
        )

        resp = User.static_request(http_methods.HTTP_METHOD_DELETE, formatted_endpoint)
        if hasattr(resp, 'error'):
            return resp
        return resp[0].user_id

    def view_push_preference(self):
        url = self.instance_url() + api_endpoints.USER_VIEW_PUSH_PREFERENCE
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def update_push_preference(self, **params):
        url = self.instance_url() + api_endpoints.USER_UPDATE_PUSH_PREFERENCE
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def reset_push_preference(self):
        url = self.instance_url() + api_endpoints.USER_RESET_PUSH_PREFERENCE
        return self.request(http_methods.HTTP_METHOD_DELETE, url)

    def view_push_preference_for_channel(self, **params):
        formatted_endpoint = api_endpoints.USER_VIEW_PUSH_PREFERENCE_FOR_CHANNEL.format(
            channel_url=params.get('channel_url')
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def update_push_preference_for_channel(self, **params):
        formatted_endpoint = api_endpoints.USER_UPDATE_PUSH_PREFERENCE_FOR_CHANNEL.format(
            channel_url=params.get('channel_url')
        )

        enable = params.get('enable', True)
        params['enable'] = enable

        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_PUT, url, params)

    def list_muted_channels(self):
        url = self.instance_url() + api_endpoints.USER_LIST_MUTED_CHANNELS
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def list_banned_channels(self):
        url = self.instance_url() + api_endpoints.USER_LIST_BANNED_CHANNELS
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def view_channel_invite_preference(self):
        url = self.instance_url() + api_endpoints.USER_VIEW_CHANNEL_INVITE_PREFERENCE
        return self.request(http_methods.HTTP_METHOD_GET, url)

    def update_channel_invite_preference(self, auto_accept=True):
        url = self.instance_url() + api_endpoints.USER_UPDATE_CHANNEL_INVITE_PREFERENCE
        params = {
            'auto_accept': auto_accept,
        }
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def choose_push_message_template(self, **params):
        url = self.instance_url() + api_endpoints.USER_CHOOSE_PUSH_MESSAGE_TEMPLATE
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params)

    def view_unread_channel_count(self, **params):
        url = self.instance_url() + api_endpoints.USER_UNREAD_CHANNEL_COUNT
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params).unread_count

    def view_group_channel_count_by_join_status(self, **params):
        url = self.instance_url() + api_endpoints.USER_VIEW_GROUP_CHANNEL_COUNT_BY_JOIN_STATUS
        return self.request(http_methods.HTTP_METHOD_GET, url, params=params).group_channel_count

    def view_count_preference_of_channel(self, channel_url=None):
        formatted_endpoint = api_endpoints.USER_COUNT_PREFERENCE_OF_CHANNEL.format(
            channel_url=channel_url
        )
        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_GET, url).count_preference

    def update_count_preference_of_channel(self, **params):
        formatted_endpoint = api_endpoints.USER_UPDATE_COUNT_PREFERENCE_OF_CHANNEL.format(
            channel_url=params.get('channel_url')
        )

        count_preference = params.get('count_preference', unread_count_preferences.ALL)
        params['count_preference'] = count_preference

        url = self.instance_url() + formatted_endpoint
        return self.request(http_methods.HTTP_METHOD_PUT, url, params=params).count_preference

    def ban_from_channel_with_custom_types(self, channel_custom_types=[]):
        url = self.instance_url() + api_endpoints.USER_BAN_FROM_CHANNELS_WITH_CUSTOM_TYPES
        params = {
            'channel_custom_types': channel_custom_types,
        }
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)

    def mute_from_channel_with_custom_types(self, channel_custom_types=[]):
        url = self.instance_url() + api_endpoints.USER_MUTE_FROM_CHANNELS_WITH_CUSTOM_TYPES
        params = {
            'channel_custom_types': channel_custom_types,
        }
        return self.request(http_methods.HTTP_METHOD_POST, url, params=params)
