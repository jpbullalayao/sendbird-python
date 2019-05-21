class SendbirdObject(dict):
    def __init__(self, pk, api_token=None, **params):
        super(SendbirdObject, self).__init__()

        object.__setattr__(self, "api_token", api_token)

        if pk:
            pk_field = self.get_pk_field()
            self[pk_field] = pk

    def __setattr__(self, k, v):
        self[k] = v
        return None

    def __getattr__(self, k):
        return self[k]

    @classmethod
    def get_pk_field(cls):
        return cls.FIELD_PK

    @classmethod
    def construct_from(cls, resp):
        instance = cls(resp.get(cls.get_pk_field()))
        instance.refresh_from(resp)
        return instance

    def refresh_from(self, values):
        for k, v in values.iteritems():
            super(SendbirdObject, self).__setitem__(k, v)
