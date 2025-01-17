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


class ConsentRenew(BaseModel):
    # Timestamp indicating when the end-user consented to these legal agreements
    agreed_at: str = Field(alias='agreedAt')

    # Originating client IP address of the end-user's computer when they consented to these legal agreements
    agreed_by: str = Field(alias='agreedBy')

    # Currency in which the `price` is listed
    currency: str = Field(alias='currency')

    # Price of the domain excluding taxes or fees. Please use GET /v2/customers/{customerId}/domains/{domain} to retrieve the renewal price and currency for the domain
    price: int = Field(alias='price')

    # Only required for hosted registrar if domain is premium. If true indicates that the `price` and `currency` listed are the registry premium price and currency for the domain
    registry_premium_pricing: typing.Optional[bool] = Field(None, alias='registryPremiumPricing')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
