import abc


class SendbirdObject(dict):
    def __init__(self, pk, api_token=None, **params):
        super(SendbirdObject, self).__init__()

        if pk:
            pk_field = self.get_pk_field()
            self[pk_field] = pk

    @classmethod
    def get_pk_field(cls):
        return cls.PK_FIELD

    def refresh_from(self, values):
        for k, v in values.iteritems():
            self[k] = v
        
