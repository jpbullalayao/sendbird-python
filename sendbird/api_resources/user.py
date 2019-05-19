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
    PK_FIELD = "user_id"

    PROFILE_URL_FIELD = "profile_url"
    DEFAULT_PROFILE_URL = ""

    @classmethod
    def create(
        cls,
        api_token=None,
        **params
    ):
    	profile_url = params.get(cls.PROFILE_URL_FIELD, cls.DEFAULT_PROFILE_URL)
    	params[cls.PROFILE_URL_FIELD] = profile_url
    	super(User, cls).create(api_token=api_token, **params)

    def instance_url(self):
        pk = self.get(self.PK_FIELD)

        base = self.class_url()
        return "{base}/{pk}".format(
            base=base,
            pk=pk
        )


