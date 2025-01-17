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

from godaddy_python_sdk.pydantic.json_data_type import JsonDataType

class JsonProperty(BaseModel):
    required: bool = Field(alias='required')

    type: str = Field(alias='type')

    default_value: typing.Optional[str] = Field(None, alias='defaultValue')

    format: typing.Optional[str] = Field(None, alias='format')

    items: typing.Optional[typing.List[JsonDataType]] = Field(None, alias='items')

    max_items: typing.Optional[int] = Field(None, alias='maxItems')

    maximum: typing.Optional[int] = Field(None, alias='maximum')

    min_items: typing.Optional[int] = Field(None, alias='minItems')

    minimum: typing.Optional[int] = Field(None, alias='minimum')

    pattern: typing.Optional[str] = Field(None, alias='pattern')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
