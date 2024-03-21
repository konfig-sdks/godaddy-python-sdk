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

from godaddy_python_sdk.pydantic.domain_available_error import DomainAvailableError
from godaddy_python_sdk.pydantic.domain_available_response import DomainAvailableResponse

class DomainAvailableBulkMixed(BaseModel):
    # Domain available response array
    domains: typing.List[DomainAvailableResponse] = Field(alias='domains')

    # Errors encountered while performing a domain available check
    errors: typing.Optional[typing.List[DomainAvailableError]] = Field(None, alias='errors')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
