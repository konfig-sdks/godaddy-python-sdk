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

from godaddy_python_sdk.pydantic.contact_domain_create import ContactDomainCreate

class DomainContactsCreateV2(BaseModel):
    admin: typing.Optional[ContactDomainCreate] = Field(None, alias='admin')

    # Unique identifier of the contact that the user wants to use for the domain admin contact. This can be specified instead of the `admin` property. 
    admin_id: typing.Optional[str] = Field(None, alias='adminId')

    billing: typing.Optional[ContactDomainCreate] = Field(None, alias='billing')

    # Unique identifier of the contact that the user wants to use for the domain billing contact. This can be specified instead of the `billing` property. 
    billing_id: typing.Optional[str] = Field(None, alias='billingId')

    registrant: typing.Optional[ContactDomainCreate] = Field(None, alias='registrant')

    # Unique identifier of the contact that the user wants to use for the domain registrant contact. This can be specified instead of the `registrant` property. 
    registrant_id: typing.Optional[str] = Field(None, alias='registrantId')

    tech: typing.Optional[ContactDomainCreate] = Field(None, alias='tech')

    # Unique identifier of the contact that the user wants to use for the domain tech contact. This can be specified instead of the `tech` property. 
    tech_id: typing.Optional[str] = Field(None, alias='techId')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
