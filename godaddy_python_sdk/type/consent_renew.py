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


class RequiredConsentRenew(TypedDict):
    # Timestamp indicating when the end-user consented to these legal agreements
    agreedAt: str

    # Originating client IP address of the end-user's computer when they consented to these legal agreements
    agreedBy: str

    # Currency in which the `price` is listed
    currency: str

    # Price of the domain excluding taxes or fees. Please use GET /v2/customers/{customerId}/domains/{domain} to retrieve the renewal price and currency for the domain
    price: int

class OptionalConsentRenew(TypedDict, total=False):
    # Only required for hosted registrar if domain is premium. If true indicates that the `price` and `currency` listed are the registry premium price and currency for the domain
    registryPremiumPricing: bool

class ConsentRenew(RequiredConsentRenew, OptionalConsentRenew):
    pass
