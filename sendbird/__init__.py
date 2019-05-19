# API resources
from sendbird.api_resources import *  # NOQA

api_token = None
api_app_id = None
api_base = "https://api-{app_id}.sendbird.com/v3/".format(
    app_id=api_app_id
)
