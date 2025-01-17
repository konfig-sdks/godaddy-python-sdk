# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from godaddy_python_sdk.pydantic.consent_domain_update import ConsentDomainUpdate

class DomainUpdate(BaseModel):
    consent: typing.Optional[ConsentDomainUpdate] = Field(None, alias='consent')

    # Whether or not the domain contact details should be shown in the WHOIS
    expose_whois: typing.Optional[bool] = Field(None, alias='exposeWhois')

    # Whether or not the domain should be locked to prevent transfers
    locked: typing.Optional[bool] = Field(None, alias='locked')

    # Fully-qualified domain names for Name Servers to associate with the domain
    name_servers: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='nameServers')

    # Whether or not the domain should be configured to automatically renew
    renew_auto: typing.Optional[bool] = Field(None, alias='renewAuto')

    # Reseller subaccount shopperid who can manage the domain
    subaccount_id: typing.Optional[str] = Field(None, alias='subaccountId')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
