# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from godaddy_python_sdk.paths.v2_customers_customer_id_domains_domain_actions_type.delete import CancelRecentAction
from godaddy_python_sdk.paths.v2_customers_customer_id_domains_domain_actions_type.get import GetRecentAction
from godaddy_python_sdk.paths.v2_customers_customer_id_domains_domain_actions.get import GetRecentList
from godaddy_python_sdk.apis.tags.actions_api_raw import ActionsApiRaw


class ActionsApi(
    CancelRecentAction,
    GetRecentAction,
    GetRecentList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ActionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ActionsApiRaw(api_client)