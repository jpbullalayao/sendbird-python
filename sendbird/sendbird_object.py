import abc


class SendbirdObject(dict):
    def __init__(self, pk, api_token=None, **params):
        super(SendbirdObject, self).__init__()

        pk_field = self.__class__.get_pk_field()

        if pk:
            setattr(self, pk_field, pk)

    @classmethod
    def get_pk_field(cls):
        return cls.PK_FIELD

    def refresh_from(self):
        pass
