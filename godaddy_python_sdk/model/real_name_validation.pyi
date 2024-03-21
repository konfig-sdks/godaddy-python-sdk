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


class RealNameValidation(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("APPROVED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def PENDING_ASSOCIATION_WITH_DOMAIN(cls):
                    return cls("PENDING_ASSOCIATION_WITH_DOMAIN")
                
                @schemas.classproperty
                def PENDING_SUBMISSION_TO_VERIFICATION_SERVICE(cls):
                    return cls("PENDING_SUBMISSION_TO_VERIFICATION_SERVICE")
                
                @schemas.classproperty
                def PENDING_VERIFICATION_SERVICE_REPLY(cls):
                    return cls("PENDING_VERIFICATION_SERVICE_REPLY")
                
                @schemas.classproperty
                def PENDING_SUBMISSION_TO_REGISTRY(cls):
                    return cls("PENDING_SUBMISSION_TO_REGISTRY")
                
                @schemas.classproperty
                def PENDING_REGISTRY_REPLY(cls):
                    return cls("PENDING_REGISTRY_REPLY")
                
                @schemas.classproperty
                def PENDING_DOMAIN_UPDATE(cls):
                    return cls("PENDING_DOMAIN_UPDATE")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
            __annotations__ = {
                "status": status,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RealNameValidation':
        return super().__new__(
            cls,
            *args,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
