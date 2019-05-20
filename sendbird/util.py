from sendbird import api_resources
from sendbird.sendbird_response import SendbirdResponse
from sendbird.sendbird_object import SendbirdObject

RESOURCE_CLASSES = {
    api_resources.GroupChannel.RESOURCE_NAME: api_resources.GroupChannel,
    api_resources.Message.RESOURCE_NAME: api_resources.Message,
    api_resources.OpenChannel.RESOURCE_NAME: api_resources.OpenChannel,
    api_resources.User.RESOURCE_NAME: api_resources.User,
}


def convert_to_sendbird_object(resp):
    if isinstance(resp, SendbirdResponse):
        sendbird_response = resp
        resp = sendbird_response.data

    if isinstance(resp, list):
        return [
            convert_to_sendbird_object(result) for result in resp
        ]

    elif isinstance(resp, dict) and not isinstance(
        resp, SendbirdObject
    ):
        # get object from resp
        # use object to call .refresh_from(), return that
        return resp

    else:
        return resp
