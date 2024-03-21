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


class VerificationRealName(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "status",
        }
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "APPROVED": "APPROVED",
                        "PENDING": "PENDING",
                        "REJECTED_DOCUMENT_OUTDATED": "REJECTED_DOCUMENT_OUTDATED",
                        "REJECTED_EXPIRED_BUSINESS_LICENSE": "REJECTED_EXPIRED_BUSINESS_LICENSE",
                        "REJECTED_EXPIRED_ORGANIZATION_CODE": "REJECTED_EXPIRED_ORGANIZATION_CODE",
                        "REJECTED_ILLEGIBLE_DOCUMENT_NAME": "REJECTED_ILLEGIBLE_DOCUMENT_NAME",
                        "REJECTED_ILLEGIBLE_IDENTIFICATION": "REJECTED_ILLEGIBLE_IDENTIFICATION",
                        "REJECTED_INCOMPLETE_IDENTIFICATION": "REJECTED_INCOMPLETE_IDENTIFICATION",
                        "REJECTED_INCOMPLETE_REGISTRATION_LETTER": "REJECTED_INCOMPLETE_REGISTRATION_LETTER",
                        "REJECTED_INCONSISTENT_IDENTITY_CARD": "REJECTED_INCONSISTENT_IDENTITY_CARD",
                        "REJECTED_INCONSISTENT_ORGANIZATION_CODE": "REJECTED_INCONSISTENT_ORGANIZATION_CODE",
                        "REJECTED_INCONSISTENT_REGISTRANT_NAME": "REJECTED_INCONSISTENT_REGISTRANT_NAME",
                        "REJECTED_INVALID_BUSINESS_LICENSE_OR_ORGANIZATION_CODE": "REJECTED_INVALID_BUSINESS_LICENSE_OR_ORGANIZATION_CODE",
                        "REJECTED_INVALID_DOCUMENT": "REJECTED_INVALID_DOCUMENT",
                        "REJECTED_MISMATCH_BUSINESS_ID": "REJECTED_MISMATCH_BUSINESS_ID",
                        "REJECTED_MISMATCH_BUSINESS_NAME": "REJECTED_MISMATCH_BUSINESS_NAME",
                        "REJECTED_MISMATCH_DOCUMENT_ID": "REJECTED_MISMATCH_DOCUMENT_ID",
                        "REJECTED_MISMATCH_DOCUMENT_NAME": "REJECTED_MISMATCH_DOCUMENT_NAME",
                        "REJECTED_MISMATCH_DOCUMENT_TYPE": "REJECTED_MISMATCH_DOCUMENT_TYPE",
                        "REJECTED_MISMATCH_REGISTRANT_INFO": "REJECTED_MISMATCH_REGISTRANT_INFO",
                        "REJECTED_MISMATCH_REGISTRANT_LOCALITY": "REJECTED_MISMATCH_REGISTRANT_LOCALITY",
                        "REJECTED_MISMATCH_REGISTRANT_NAME": "REJECTED_MISMATCH_REGISTRANT_NAME",
                        "REJECTED_UNABLE_TO_OPEN": "REJECTED_UNABLE_TO_OPEN",
                        "REJECTED_UNABLE_TO_VERIFY": "REJECTED_UNABLE_TO_VERIFY",
                        "REJECTED_UNKNOWN_ERROR": "REJECTED_UNKNOWN_ERROR",
                        "UNABLE_TO_RETRIEVE_STATUS": "UNABLE_TO_RETRIEVE_STATUS",
                    }
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("APPROVED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def REJECTED_DOCUMENT_OUTDATED(cls):
                    return cls("REJECTED_DOCUMENT_OUTDATED")
                
                @schemas.classproperty
                def REJECTED_EXPIRED_BUSINESS_LICENSE(cls):
                    return cls("REJECTED_EXPIRED_BUSINESS_LICENSE")
                
                @schemas.classproperty
                def REJECTED_EXPIRED_ORGANIZATION_CODE(cls):
                    return cls("REJECTED_EXPIRED_ORGANIZATION_CODE")
                
                @schemas.classproperty
                def REJECTED_ILLEGIBLE_DOCUMENT_NAME(cls):
                    return cls("REJECTED_ILLEGIBLE_DOCUMENT_NAME")
                
                @schemas.classproperty
                def REJECTED_ILLEGIBLE_IDENTIFICATION(cls):
                    return cls("REJECTED_ILLEGIBLE_IDENTIFICATION")
                
                @schemas.classproperty
                def REJECTED_INCOMPLETE_IDENTIFICATION(cls):
                    return cls("REJECTED_INCOMPLETE_IDENTIFICATION")
                
                @schemas.classproperty
                def REJECTED_INCOMPLETE_REGISTRATION_LETTER(cls):
                    return cls("REJECTED_INCOMPLETE_REGISTRATION_LETTER")
                
                @schemas.classproperty
                def REJECTED_INCONSISTENT_IDENTITY_CARD(cls):
                    return cls("REJECTED_INCONSISTENT_IDENTITY_CARD")
                
                @schemas.classproperty
                def REJECTED_INCONSISTENT_ORGANIZATION_CODE(cls):
                    return cls("REJECTED_INCONSISTENT_ORGANIZATION_CODE")
                
                @schemas.classproperty
                def REJECTED_INCONSISTENT_REGISTRANT_NAME(cls):
                    return cls("REJECTED_INCONSISTENT_REGISTRANT_NAME")
                
                @schemas.classproperty
                def REJECTED_INVALID_BUSINESS_LICENSE_OR_ORGANIZATION_CODE(cls):
                    return cls("REJECTED_INVALID_BUSINESS_LICENSE_OR_ORGANIZATION_CODE")
                
                @schemas.classproperty
                def REJECTED_INVALID_DOCUMENT(cls):
                    return cls("REJECTED_INVALID_DOCUMENT")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_BUSINESS_ID(cls):
                    return cls("REJECTED_MISMATCH_BUSINESS_ID")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_BUSINESS_NAME(cls):
                    return cls("REJECTED_MISMATCH_BUSINESS_NAME")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_DOCUMENT_ID(cls):
                    return cls("REJECTED_MISMATCH_DOCUMENT_ID")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_DOCUMENT_NAME(cls):
                    return cls("REJECTED_MISMATCH_DOCUMENT_NAME")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_DOCUMENT_TYPE(cls):
                    return cls("REJECTED_MISMATCH_DOCUMENT_TYPE")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_REGISTRANT_INFO(cls):
                    return cls("REJECTED_MISMATCH_REGISTRANT_INFO")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_REGISTRANT_LOCALITY(cls):
                    return cls("REJECTED_MISMATCH_REGISTRANT_LOCALITY")
                
                @schemas.classproperty
                def REJECTED_MISMATCH_REGISTRANT_NAME(cls):
                    return cls("REJECTED_MISMATCH_REGISTRANT_NAME")
                
                @schemas.classproperty
                def REJECTED_UNABLE_TO_OPEN(cls):
                    return cls("REJECTED_UNABLE_TO_OPEN")
                
                @schemas.classproperty
                def REJECTED_UNABLE_TO_VERIFY(cls):
                    return cls("REJECTED_UNABLE_TO_VERIFY")
                
                @schemas.classproperty
                def REJECTED_UNKNOWN_ERROR(cls):
                    return cls("REJECTED_UNKNOWN_ERROR")
                
                @schemas.classproperty
                def UNABLE_TO_RETRIEVE_STATUS(cls):
                    return cls("UNABLE_TO_RETRIEVE_STATUS")
            __annotations__ = {
                "status": status,
            }

    
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VerificationRealName':
        return super().__new__(
            cls,
            *args,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
