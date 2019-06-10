# All endpoint constants that both the OpenChannel and GroupChannel
# resources share
CHANNEL_BAN_USER = "/ban"
CHANNEL_FREEZE = "/freeze"
CHANNEL_LIST_BANNED_USERS = "/ban"
CHANNEL_LIST_MUTED_USERS = "/mute"
CHANNEL_MUTE_USER = "/mute"
CHANNEL_UNBAN_USER = "/ban/{banned_user_id}"
CHANNEL_UNMUTE_USER = "/mute/{muted_user_id}"
CHANNEL_UPDATE_BAN = "/ban/{banned_user_id}"
CHANNEL_VIEW_BAN = "/ban/{banned_user_id}"
CHANNEL_VIEW_MUTE = "/mute/{muted_user_id}"

CHANNEL_DELETE_MESSAGE = "/messages/{message_id}"
CHANNEL_LIST_MESSAGES = "/messages"
CHANNEL_MARK_AS_READ = "/messages/mark_as_read"
CHANNEL_SEND_MESSAGE = "/messages"
CHANNEL_UPDATE_MESSAGE = "/messages/{message_id}"
CHANNEL_VIEW_MEMBER_UNNREAD_COUNT = "/messages/unread_count"
CHANNEL_VIEW_MESSAGE = "/messages/{message_id}"
CHANNEL_VIEW_MESSAGE_COUNT = "/messages/total_count"

CHANNEL_CREATE_METADATA = "/metadata"
CHANNEL_VIEW_METADATA = "/metadata"
