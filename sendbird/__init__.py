# API resources
from sendbird.api_resources import *  # NOQA

api_key = None
api_application_id = None
api_base = "http://api-{application_id}.sendbird.com/v3/".format(
	application_id=api_application_id
)
