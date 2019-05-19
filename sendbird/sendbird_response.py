import json


class SendbirdResponse(object):
    def __init__(self, body):
        self.body = body
        self.data = json.loads(body)
