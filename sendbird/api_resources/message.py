from sendbird.api_resources.abstract.createable_api_resource import CreateableAPIResource  # NOQA
from sendbird.api_resources.abstract.deletable_api_resource import DeletableAPIResource  # NOQA
from sendbird.api_resources.abstract.listable_api_resource import ListableAPIResource  # NOQA
from sendbird.api_resources.abstract.updateable_api_resource import UpdateableAPIResource  # NOQA


class Message(
	CreateableAPIResource,
	DeletableAPIResource,
	ListableAPIResource,
	UpdateableAPIResource
):
    pass
