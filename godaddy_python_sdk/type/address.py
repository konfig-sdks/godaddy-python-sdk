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


class RequiredAddress(TypedDict):
    address1: str

    city: str

    # Two-letter ISO country code to be used as a hint for target region<br/><br/> NOTE: These are sample values, there are many <a href='http://www.iso.org/iso/country_codes.htm'>more</a>
    country: str

    # Postal or zip code
    postalCode: str

    # State or province or territory
    state: str

class OptionalAddress(TypedDict, total=False):
    address2: str

class Address(RequiredAddress, OptionalAddress):
    pass