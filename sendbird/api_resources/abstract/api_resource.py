import abc

from sendbird.http_methods import HTTP_METHOD_GET


class APIResource:
    @classmethod
    def retrieve(cls, pk, api_token=None, **params):
        instance = cls(pk, api_token, **params)
        instance.refresh()
        return instance

    def refresh(self):
        # self.refresh_from(self.instance_url())
        # return self
        pass

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform "
                "actions on its subclasses (e.g. Message)"
            )
        return '{resource_name}s'.format(resource_name=cls.RESOURCE_NAME)

    @abc.abstractproperty
    def instance_url(self):
        raise NotImplementedError
