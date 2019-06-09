from sendbird import api_endpoints 
from sendbird import http_methods
from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updatable_api_resource import UpdatableAPIResource  # NOQA


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
