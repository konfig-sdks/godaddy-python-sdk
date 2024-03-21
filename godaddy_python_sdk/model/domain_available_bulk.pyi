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


class DomainAvailableBulk(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "domains",
        }
        
        class properties:
            
            
            class domains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DomainAvailableResponse']:
                        return DomainAvailableResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DomainAvailableResponse'], typing.List['DomainAvailableResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'domains':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DomainAvailableResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "domains": domains,
            }

    
    domains: MetaOapg.properties.domains
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domains"]) -> MetaOapg.properties.domains: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["domains", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domains"]) -> MetaOapg.properties.domains: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["domains", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        domains: typing.Union[MetaOapg.properties.domains, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DomainAvailableBulk':
        return super().__new__(
            cls,
            *args,
            domains=domains,
            _configuration=_configuration,
            **kwargs,
        )

from godaddy_python_sdk.model.domain_available_response import DomainAvailableResponse
