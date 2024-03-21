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

from godaddy_python_sdk.pydantic.address import Address

class ContactDomainCreate(BaseModel):
    address_mailing: Address = Field(alias='addressMailing')

    email: str = Field(alias='email')

    # The encoding of the contact data<br/><ul><li><strong style='margin-left: 12px;'>ASCII</strong> - Data contains only ASCII characters that are not region or language specific</li><li><strong style='margin-left: 12px;'>UTF-8</strong> - Data contains characters that are specific to a region or language</li></ul>
    encoding: Literal["ASCII", "UTF-8"] = Field(alias='encoding')

    name_first: str = Field(alias='nameFirst')

    name_last: str = Field(alias='nameLast')

    phone: str = Field(alias='phone')

    fax: typing.Optional[str] = Field(None, alias='fax')

    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    # The contact eligibility data fields as specified by GET /v2/customers/{customerId}/domains/contacts/schema/{tld}
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    name_middle: typing.Optional[str] = Field(None, alias='nameMiddle')

    organization: typing.Optional[str] = Field(None, alias='organization')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
