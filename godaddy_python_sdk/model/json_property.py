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


class JsonProperty(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
            "$ref",
            "required",
        }
        
        class properties:
            required = schemas.BoolSchema
            type = schemas.StrSchema
            defaultValue = schemas.StrSchema
            format = schemas.StrSchema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JsonDataType']:
                        return JsonDataType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JsonDataType'], typing.List['JsonDataType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JsonDataType':
                    return super().__getitem__(i)
            maxItems = schemas.IntSchema
            maximum = schemas.IntSchema
            minItems = schemas.IntSchema
            minimum = schemas.IntSchema
            pattern = schemas.StrSchema
            __annotations__ = {
                "required": required,
                "type": type,
                "defaultValue": defaultValue,
                "format": format,
                "items": items,
                "maxItems": maxItems,
                "maximum": maximum,
                "minItems": minItems,
                "minimum": minimum,
                "pattern": pattern,
            }

    
    type: MetaOapg.properties.type
    required: MetaOapg.properties.required
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxItems"]) -> MetaOapg.properties.maxItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximum"]) -> MetaOapg.properties.maximum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minItems"]) -> MetaOapg.properties.minItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum"]) -> MetaOapg.properties.minimum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern"]) -> MetaOapg.properties.pattern: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["required", "type", "defaultValue", "format", "items", "maxItems", "maximum", "minItems", "minimum", "pattern", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union[MetaOapg.properties.format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxItems"]) -> typing.Union[MetaOapg.properties.maxItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximum"]) -> typing.Union[MetaOapg.properties.maximum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minItems"]) -> typing.Union[MetaOapg.properties.minItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum"]) -> typing.Union[MetaOapg.properties.minimum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pattern"]) -> typing.Union[MetaOapg.properties.pattern, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["required", "type", "defaultValue", "format", "items", "maxItems", "maximum", "minItems", "minimum", "pattern", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        required: typing.Union[MetaOapg.properties.required, bool, ],
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, str, schemas.Unset] = schemas.unset,
        format: typing.Union[MetaOapg.properties.format, str, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        maxItems: typing.Union[MetaOapg.properties.maxItems, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maximum: typing.Union[MetaOapg.properties.maximum, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minItems: typing.Union[MetaOapg.properties.minItems, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minimum: typing.Union[MetaOapg.properties.minimum, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pattern: typing.Union[MetaOapg.properties.pattern, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonProperty':
        return super().__new__(
            cls,
            *args,
            type=type,
            required=required,
            defaultValue=defaultValue,
            format=format,
            items=items,
            maxItems=maxItems,
            maximum=maximum,
            minItems=minItems,
            minimum=minimum,
            pattern=pattern,
            _configuration=_configuration,
            **kwargs,
        )

from godaddy_python_sdk.model.json_data_type import JsonDataType
