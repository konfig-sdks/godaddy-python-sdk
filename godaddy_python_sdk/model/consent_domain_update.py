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


class ConsentDomainUpdate(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "agreedAt",
            "agreedBy",
            "agreementKeys",
        }
        
        class properties:
            agreedAt = schemas.StrSchema
            agreedBy = schemas.StrSchema
            
            
            class agreementKeys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "EXPOSE_WHOIS": "EXPOSE_WHOIS",
                            }
                        
                        @schemas.classproperty
                        def EXPOSE_WHOIS(cls):
                            return cls("EXPOSE_WHOIS")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agreementKeys':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "agreedAt": agreedAt,
                "agreedBy": agreedBy,
                "agreementKeys": agreementKeys,
            }

    
    agreedAt: MetaOapg.properties.agreedAt
    agreedBy: MetaOapg.properties.agreedBy
    agreementKeys: MetaOapg.properties.agreementKeys
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreementKeys"]) -> MetaOapg.properties.agreementKeys: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agreedAt", "agreedBy", "agreementKeys", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreementKeys"]) -> MetaOapg.properties.agreementKeys: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agreedAt", "agreedBy", "agreementKeys", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        agreedAt: typing.Union[MetaOapg.properties.agreedAt, str, ],
        agreedBy: typing.Union[MetaOapg.properties.agreedBy, str, ],
        agreementKeys: typing.Union[MetaOapg.properties.agreementKeys, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConsentDomainUpdate':
        return super().__new__(
            cls,
            *args,
            agreedAt=agreedAt,
            agreedBy=agreedBy,
            agreementKeys=agreementKeys,
            _configuration=_configuration,
            **kwargs,
        )
