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


class DomainAvailableError(BaseModel):
    # Short identifier for the error, suitable for indicating the specific error within client code
    code: str = Field(alias='code')

    # Domain name
    domain: str = Field(alias='domain')

    # <ul> <li style='margin-left: 12px;'>JSONPath referring to a field containing an error</li> <strong style='margin-left: 12px;'>OR</strong> <li style='margin-left: 12px;'>JSONPath referring to a field that refers to an object containing an error, with more detail in `pathRelated`</li> </ul>
    path: str = Field(alias='path')

    # HTTP status code that would return for a single check
    status: int = Field(alias='status')

    # Human-readable, English description of the error
    message: typing.Optional[str] = Field(None, alias='message')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
