# All endpoint constants for the User resource
USER_ADD_DEVICE_TOKEN = "/push/{token_type}"
USER_BAN_FROM_CHANNELS_WITH_CUSTOM_TYPES = "/banned_channel_custom_types"
USER_BLOCK = "/block"
USER_CHOOSE_PUSH_MESSAGE_TEMPLATE = "/push/template"
USER_LIST_BANNED_CHANNELS = "/ban"
USER_LIST_BLOCKED_USERS = "/block"
USER_LIST_DEVICE_TOKENS = "/push/{token_type}"
USER_LIST_MUTED_CHANNELS = "/mute"
USER_MARK_AS_READ_ALL = "/mark_as_read_all"
USER_MUTE_FROM_CHANNELS_WITH_CUSTOM_TYPES = "/muted_channel_custom_types"
USER_MY_GROUP_CHANNELS = "/my_group_channels"
USER_REGISTER_OPERATOR_CHANNELS_CUSTOM_TYPES = "/operating_channel_custom_types"
USER_REMOVE_ALL_DEVICE_TOKENS = "/push"
USER_REMOVE_DEVICE_TOKEN = "/push/{token_type}/{token}"
USER_REMOVE_DEVICE_TOKEN_FROM_OWNER = "/push/device_tokens/{token_type}/{token}"
USER_RESET_PUSH_PREFERENCE = "/push_preference"
USER_UNBLOCK = "/block/{target_id}"
USER_UNREAD_CHANNEL_COUNT = "/unread_channel_count"
USER_UNREAD_ITEM_COUNT = "/unread_item_count"
USER_UNREAD_MESSAGE_COUNT = "/unread_message_count"
USER_UPDATE_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
USER_UPDATE_COUNT_PREFERENCE_OF_CHANNEL = "/count_preference/{channel_url}"
USER_UPDATE_PUSH_PREFERENCE = "/push_preference"
USER_UPDATE_PUSH_PREFERENCE_FOR_CHANNEL = "/push_preference/{channel_url}"
USER_VIEW_CHANNEL_INVITE_PREFERENCE = "/channel_invitation_preference"
USER_COUNT_PREFERENCE_OF_CHANNEL = "/count_preference/{channel_url}"
USER_VIEW_DEVICE_TOKEN_OWNER = "/push/device_tokens/{token_type}/{token}"
USER_VIEW_GROUP_CHANNEL_COUNT_BY_JOIN_STATUS = "/group_channel_count"
USER_VIEW_PUSH_PREFERENCE = "/push_preference"
USER_VIEW_PUSH_PREFERENCE_FOR_CHANNEL = "/push_preference/{channel_url}"

USER_CREATE_METADATA = "/metadata"
USER_UPDATE_METADATA = "/metadata"
USER_VIEW_METADATA = "/metadata"
