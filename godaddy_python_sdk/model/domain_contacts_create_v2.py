# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from godaddy_python_sdk import schemas  # noqa: F401


class DomainContactsCreateV2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def admin() -> typing.Type['ContactDomainCreate']:
                return ContactDomainCreate
            adminId = schemas.StrSchema
        
            @staticmethod
            def billing() -> typing.Type['ContactDomainCreate']:
                return ContactDomainCreate
            billingId = schemas.StrSchema
        
            @staticmethod
            def registrant() -> typing.Type['ContactDomainCreate']:
                return ContactDomainCreate
            registrantId = schemas.StrSchema
        
            @staticmethod
            def tech() -> typing.Type['ContactDomainCreate']:
                return ContactDomainCreate
            techId = schemas.StrSchema
            __annotations__ = {
                "admin": admin,
                "adminId": adminId,
                "billing": billing,
                "billingId": billingId,
                "registrant": registrant,
                "registrantId": registrantId,
                "tech": tech,
                "techId": techId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin"]) -> 'ContactDomainCreate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adminId"]) -> MetaOapg.properties.adminId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing"]) -> 'ContactDomainCreate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingId"]) -> MetaOapg.properties.billingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registrant"]) -> 'ContactDomainCreate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registrantId"]) -> MetaOapg.properties.registrantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tech"]) -> 'ContactDomainCreate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["techId"]) -> MetaOapg.properties.techId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["admin", "adminId", "billing", "billingId", "registrant", "registrantId", "tech", "techId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin"]) -> typing.Union['ContactDomainCreate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adminId"]) -> typing.Union[MetaOapg.properties.adminId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing"]) -> typing.Union['ContactDomainCreate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingId"]) -> typing.Union[MetaOapg.properties.billingId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registrant"]) -> typing.Union['ContactDomainCreate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registrantId"]) -> typing.Union[MetaOapg.properties.registrantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tech"]) -> typing.Union['ContactDomainCreate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["techId"]) -> typing.Union[MetaOapg.properties.techId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admin", "adminId", "billing", "billingId", "registrant", "registrantId", "tech", "techId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        admin: typing.Union['ContactDomainCreate', schemas.Unset] = schemas.unset,
        adminId: typing.Union[MetaOapg.properties.adminId, str, schemas.Unset] = schemas.unset,
        billing: typing.Union['ContactDomainCreate', schemas.Unset] = schemas.unset,
        billingId: typing.Union[MetaOapg.properties.billingId, str, schemas.Unset] = schemas.unset,
        registrant: typing.Union['ContactDomainCreate', schemas.Unset] = schemas.unset,
        registrantId: typing.Union[MetaOapg.properties.registrantId, str, schemas.Unset] = schemas.unset,
        tech: typing.Union['ContactDomainCreate', schemas.Unset] = schemas.unset,
        techId: typing.Union[MetaOapg.properties.techId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DomainContactsCreateV2':
        return super().__new__(
            cls,
            *args,
            admin=admin,
            adminId=adminId,
            billing=billing,
            billingId=billingId,
            registrant=registrant,
            registrantId=registrantId,
            tech=tech,
            techId=techId,
            _configuration=_configuration,
            **kwargs,
        )

from godaddy_python_sdk.model.contact_domain_create import ContactDomainCreate
