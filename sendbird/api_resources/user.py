from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updatable_api_resource import UpdatableAPIResource  # NOQA
from sendbird.http_methods import HTTP_METHOD_GET

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

    ENDPOINT_MY_GROUP_CHANNELS = "/my_group_channels"
    ENDPOINT_UNREAD_MESSAGE_COUNT = "/unread_message_count"

    @classmethod
    def create(
        cls,
        api_token=None,
        **params
    ):
        profile_url = params.get(cls.FIELD_PROFILE_URL, cls.DEFAULT_PROFILE_URL)
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
        url = self.instance_url() + User.ENDPOINT_MY_GROUP_CHANNELS
        return self.request(HTTP_METHOD_GET, url)
        
    def unread_message_count(self):
        url = self.instance_url() + User.ENDPOINT_UNREAD_MESSAGE_COUNT
        return self.request(HTTP_METHOD_GET, url).get('unread_count')
