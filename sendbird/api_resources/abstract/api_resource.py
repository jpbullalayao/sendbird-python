import abc


class APIResource:
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
