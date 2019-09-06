import abc
import sendbird

from sendbird import http_methods
from sendbird.api_requestor import APIRequestor
from sendbird.sendbird_object import SendbirdObject
from sendbird.util import convert_to_sendbird_object


class APIResource(SendbirdObject):
    @classmethod
    def retrieve(cls, pk, api_token=None, **params):
        requestor = APIRequestor(
            api_token
        )

        instance = cls(pk, api_token, **params)
        instance.refresh(requestor)
        return instance

    def refresh(self, requestor):
        response = requestor.request(http_methods.HTTP_METHOD_GET, self.instance_url())
        sendbird_object = convert_to_sendbird_object(response, self.__class__)
        self.refresh_from(sendbird_object)
        return self

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform "
                "actions on its subclasses (e.g. Message)"
            )
        return "{resource_name}s".format(
            resource_name=cls.RESOURCE_NAME
        )

    @abc.abstractmethod
    def instance_url(self):
        raise NotImplementedError

    @classmethod
    def static_request(cls, method, url, api_token=None, params=None, headers=None):
        requestor = APIRequestor(
            api_token or sendbird.api_token
        )
        response = requestor.request(method, url, params)
        sendbird_object = convert_to_sendbird_object(response,  cls)
        return sendbird_object

    def request(self, method, url, params=None, headers=None):
        requestor = APIRequestor(
            self.api_token,
        )
        response = requestor.request(method, url, params)
        sendbird_object = convert_to_sendbird_object(response,  self.__class__)
        return sendbird_object
