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


class DomainPurchaseResponse(BaseModel):
    # Number items included in the order
    item_count: int = Field(alias='itemCount')

    # Unique identifier of the order processed to purchase the domain
    order_id: int = Field(alias='orderId')

    # Total cost of the domain and any selected add-ons
    total: int = Field(alias='total')

    # Currency in which the `total` is listed
    currency: typing.Optional[str] = Field(None, alias='currency')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
