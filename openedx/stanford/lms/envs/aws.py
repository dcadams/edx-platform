from lms.envs.aws import *


CERT_NAME_LONG = ENV_TOKENS.get('CERT_NAME_LONG', CERT_NAME_LONG)
CERT_NAME_SHORT = ENV_TOKENS.get('CERT_NAME_SHORT', CERT_NAME_SHORT)
# TODO: Get Course Forums Download and Student Forums download
#   from env_tokens instead of common
COURSE_FORUMS_DOWNLOAD_ROUTING_KEY = HIGH_MEM_QUEUE
COURSE_MODE_DEFAULTS = ENV_TOKENS.get('COURSE_MODE_DEFAULTS', COURSE_MODE_DEFAULTS)
DISABLE_REGISTER_BUTTON = ENV_TOKENS.get('DISABLE_REGISTER_BUTTON', DISABLE_REGISTER_BUTTON)
DISPLAY_COURSE_TILES = ENV_TOKENS.get('DISPLAY_COURSE_TILES', True)
EXTRA_MIMETYPES = ENV_TOKENS.get('EXTRA_MIMETYPES', EXTRA_MIMETYPES)
FORUM_MONGO_PARAMS = AUTH_TOKENS.get('FORUM_MONGO_PARAMS', FORUM_MONGO_PARAMS)
HELP_MODAL_LINKS = ENV_TOKENS.get('HELP_MODAL_LINKS', [])
INLINE_ANALYTICS_SUPPORTED_TYPES = ENV_TOKENS.get('INLINE_ANALYTICS_SUPPORTED_TYPES', INLINE_ANALYTICS_SUPPORTED_TYPES)
MAX_ENROLLEES_FOR_METRICS_USING_DB = ENV_TOKENS.get('MAX_ENROLLEES_FOR_METRICS_USING_DB', MAX_ENROLLEES_FOR_METRICS_USING_DB)
ORA2_RESPONSES_DOWNLOAD_ROUTING_KEY = HIGH_MEM_QUEUE
ORA2_RESPONSES_DOWNLOAD = ENV_TOKENS.get("ORA2_RESPONSES_DOWNLOAD", ORA2_RESPONSES_DOWNLOAD)
PAYMENT_CONFIRM_EMAIL = ENV_TOKENS.get(
    'PAYMENT_CONFIRM_EMAIL',
    ENV_TOKENS.get(
        'PAYMENT_SUPPORT_EMAIL',
        PAYMENT_CONFIRM_EMAIL
    )
)
PAYMENT_SUPPORT_PHONE = ENV_TOKENS.get('PAYMENT_SUPPORT_PHONE', PAYMENT_SUPPORT_PHONE)
SHIB_ONLY_SITE = ENV_TOKENS.get(
    'SHIB_ONLY_SITE',
    SHIB_ONLY_SITE
)
SHIB_REDIRECT_DOMAIN_WHITELIST = ENV_TOKENS.get(
    'SHIB_REDIRECT_DOMAIN_WHITELIST',
    SHIB_REDIRECT_DOMAIN_WHITELIST
)
STUDENT_FORUMS_DOWNLOAD_ROUTING_KEY = HIGH_MEM_QUEUE
STUDENT_RESPONSES_DOWNLOAD_ROUTING_KEY = HIGH_MEM_QUEUE
STUDENT_RESPONSES_DOWNLOAD = ENV_TOKENS.get(
    'STUDENT_RESPONSES_DOWNLOAD',
    STUDENT_RESPONSES_DOWNLOAD
)

INSTRUCTOR_QUERY_PROBLEM_TYPES = ENV_TOKENS.get(
    'INSTRUCTOR_QUERY_PROBLEM_TYPES',
    INSTRUCTOR_QUERY_PROBLEM_TYPES
)
