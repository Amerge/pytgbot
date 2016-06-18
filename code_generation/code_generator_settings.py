CLASS_TYPE_PATHS__IMPORT = 0
CLASS_TYPE_PATHS__PARENT = 1
CLASS_TYPE_PATHS__DESCRIPTION = 2
CLASS_TYPE_PATHS = {  # class: import, master_class, descr
    "TgBotApiObject": ("pytgbot.api_types.", "object", None),

    # pytgbot.api_types.receivable.media.*
    "Media":                ("pytgbot.api_types.receivable.media.", "Receivable", None),
    "Voice":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Contact":              ("pytgbot.api_types.receivable.media.", "Media", None),
    "Location":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Venue":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "PhotoSize":            ("pytgbot.api_types.receivable.media.", "Result", None),
    "UserProfilePhotos":    ("pytgbot.api_types.receivable.media.", "Result", None),
    "Audio":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "Document":             ("pytgbot.api_types.receivable.media.", "Media", None),
    "Sticker":              ("pytgbot.api_types.receivable.media.", "Media", None),
    "Video":                ("pytgbot.api_types.receivable.media.", "Media", None),
    "File":                 ("pytgbot.api_types.receivable.media.", "Receivable", None),

    # pytgbot.api_types.receivable.responses.*
    "InlineQuery": ("pytgbot.api_types.receivable.", "Result", None),
    "MessageEntity": ("pytgbot.api_types.receivable.", "Result", None),

    # pytgbot.api_types.receivable.responses.peer.*
    "ChatMember":   ("pytgbot.api_types.receivable.peer.", "Result", None),
    "Peer":         ("pytgbot.api_types.receivable.peer.", "Result", None),
    "User":         ("pytgbot.api_types.receivable.peer.", "Peer", None),
    "Chat":         ("pytgbot.api_types.receivable.peer.", "Peer", None),

    # pytgbot.api_types.receivable.updates.*
    "Update":               ("pytgbot.api_types.receivable.updates.", "Receivable", None),
    "Message":              ("pytgbot.api_types.receivable.updates.", "UpdateType", None),
    "CallbackQuery":        ("pytgbot.api_types.receivable.updates.", "UpdateType", None),

    # pytgbot.api_types.receivable.inline.*
    "ChosenInlineResult":           ("pytgbot.api_types.receivable.inline.", "UpdateType", None),

    # pytgbot.api_types.sendable.inline.*
    "InputMessageContent":          ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InputTextMessageContent":      ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputLocationMessageContent":  ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputVenueMessageContent":     ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InputContactMessageContent":   ("pytgbot.api_types.sendable.inline.", "InputMessageContent", None),
    "InlineQueryResult":            ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InlineQueryResultArticle":     ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultPhoto":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultGif":         ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultMpeg4Gif":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVideo":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultAudio":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVoice":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultDocument":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultLocation":    ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultVenue":       ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultContact":     ("pytgbot.api_types.sendable.inline.", "InlineQueryResult", None),
    "InlineQueryResultCached":            ("pytgbot.api_types.sendable.inline.", "Sendable", None),
    "InlineQueryResultCachedArticle":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedPhoto":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedGif":         ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedMpeg4Gif":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedSticker":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVideo":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedAudio":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVoice":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedDocument":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedLocation":    ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedVenue":       ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),
    "InlineQueryResultCachedContact":     ("pytgbot.api_types.sendable.inline.", "InlineQueryCachedResult", None),

    # pytgbot.api_types.sendable.reply_markup.*
    "ReplyKeyboardMarkup":  ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ReplyKeyboardHide":    ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "ForceReply":           ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "InlineKeyboardMarkup": ("pytgbot.api_types.sendable.reply_markup.", "ReplyMarkup", None),
    "KeyboardButton":       ("pytgbot.api_types.sendable.reply_markup.", "Button", None),
    "InlineKeyboardButton": ("pytgbot.api_types.sendable.reply_markup.", "Button", None),

}