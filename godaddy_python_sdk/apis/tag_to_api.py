import typing_extensions

from godaddy_python_sdk.apis.tags import TagValues
from godaddy_python_sdk.apis.tags.v1_api import V1Api
from godaddy_python_sdk.apis.tags.domains_api import DomainsApi
from godaddy_python_sdk.apis.tags.notifications_api import NotificationsApi
from godaddy_python_sdk.apis.tags.actions_api import ActionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.V1: V1Api,
        TagValues.DOMAINS: DomainsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.ACTIONS: ActionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.V1: V1Api,
        TagValues.DOMAINS: DomainsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.ACTIONS: ActionsApi,
    }
)
