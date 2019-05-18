from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.createable_api_resource import ListableAPIResource  # NOQA


class Message(
	CreateableAPIResource,
	ListableAPIResource
):
    pass
