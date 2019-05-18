from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import UpdateableAPIResource  # NOQA


class Channel(
	CreateableAPIResource,
	ListableAPIResource,
	UpdateableAPIResource
):
    pass
