from sendbird.sendbird_response import SendbirdResponse
from sendbird.sendbird_object import SendbirdObject


def convert_to_sendbird_object(resp, cls):
    if isinstance(resp, SendbirdResponse):
        sendbird_response = resp
        resp = sendbird_response.data

    if isinstance(resp, list):
        return [
            convert_to_sendbird_object(result, cls) for result in resp
        ]

    elif isinstance(resp, dict) and not isinstance(
        resp, SendbirdObject
    ):
        return cls.construct_from(resp)

    else:
        return resp
