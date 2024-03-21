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


class DNSRecordCreateType(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
            "name",
        }
        
        class properties:
            data = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class port(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 65535
                    inclusive_minimum = 1
            priority = schemas.IntSchema
            protocol = schemas.StrSchema
            service = schemas.StrSchema
            ttl = schemas.IntSchema
            weight = schemas.IntSchema
            __annotations__ = {
                "data": data,
                "name": name,
                "port": port,
                "priority": priority,
                "protocol": protocol,
                "service": service,
                "ttl": ttl,
                "weight": weight,
            }

    
    data: MetaOapg.properties.data
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weight"]) -> MetaOapg.properties.weight: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "name", "port", "priority", "protocol", "service", "ttl", "weight", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service"]) -> typing.Union[MetaOapg.properties.service, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union[MetaOapg.properties.weight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "name", "port", "priority", "protocol", "service", "ttl", "weight", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        data: typing.Union[MetaOapg.properties.data, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
        service: typing.Union[MetaOapg.properties.service, str, schemas.Unset] = schemas.unset,
        ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weight: typing.Union[MetaOapg.properties.weight, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DNSRecordCreateType':
        return super().__new__(
            cls,
            *args,
            data=data,
            name=name,
            port=port,
            priority=priority,
            protocol=protocol,
            service=service,
            ttl=ttl,
            weight=weight,
            _configuration=_configuration,
            **kwargs,
        )