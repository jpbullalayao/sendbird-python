from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA


class Channel(
	CreateableAPIResource,
	ListableAPIResource,
):
    pass
