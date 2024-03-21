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

from godaddy_python_sdk.type.verification_domain_name import VerificationDomainName
from godaddy_python_sdk.type.verification_real_name import VerificationRealName

class RequiredVerificationsDomain(TypedDict):
    pass

class OptionalVerificationsDomain(TypedDict, total=False):
    domainName: VerificationDomainName

    realName: VerificationRealName

class VerificationsDomain(RequiredVerificationsDomain, OptionalVerificationsDomain):
    pass