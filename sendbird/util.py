from sendbird.sendbird_response import SendbirdResponse


def convert_to_sendbird_object(resp):
    if isinstance(resp, SendbirdResponse):
        sendbird_response = resp
        resp = sendbird_response.data

    if isinstance(resp, list):
        return [
            convert_to_sendbird_object(result) for result in resp
        ]

    return resp
