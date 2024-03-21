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


class RequiredRealNameValidation(TypedDict):
    pass

class OptionalRealNameValidation(TypedDict, total=False):
    status: str

class RealNameValidation(RequiredRealNameValidation, OptionalRealNameValidation):
    pass
