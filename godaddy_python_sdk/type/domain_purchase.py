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

from godaddy_python_sdk.type.consent import Consent
from godaddy_python_sdk.type.contact import Contact

class RequiredDomainPurchase(TypedDict):
    consent: Consent

    # For internationalized domain names with non-ascii characters, the domain name is converted to punycode before format and pattern validation rules are checked
    domain: str

class OptionalDomainPurchase(TypedDict, total=False):
    contactAdmin: Contact

    contactBilling: Contact

    contactRegistrant: Contact

    contactTech: Contact

    nameServers: typing.List[str]

    period: int

    privacy: bool

    renewAuto: bool

class DomainPurchase(RequiredDomainPurchase, OptionalDomainPurchase):
    pass