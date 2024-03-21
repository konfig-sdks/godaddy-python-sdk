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


class ConsentRedemption(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "agreedAt",
            "agreedBy",
            "price",
            "fee",
            "currency",
        }
        
        class properties:
            agreedAt = schemas.StrSchema
            agreedBy = schemas.StrSchema
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
            fee = schemas.IntSchema
            price = schemas.IntSchema
            __annotations__ = {
                "agreedAt": agreedAt,
                "agreedBy": agreedBy,
                "currency": currency,
                "fee": fee,
                "price": price,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    agreedAt: MetaOapg.properties.agreedAt
    agreedBy: MetaOapg.properties.agreedBy
    price: MetaOapg.properties.price
    fee: MetaOapg.properties.fee
    currency: MetaOapg.properties.currency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee"]) -> MetaOapg.properties.fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agreedAt"], typing_extensions.Literal["agreedBy"], typing_extensions.Literal["price"], typing_extensions.Literal["fee"], typing_extensions.Literal["currency"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee"]) -> MetaOapg.properties.fee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agreedAt"], typing_extensions.Literal["agreedBy"], typing_extensions.Literal["price"], typing_extensions.Literal["fee"], typing_extensions.Literal["currency"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agreedAt: typing.Union[MetaOapg.properties.agreedAt, str, ],
        agreedBy: typing.Union[MetaOapg.properties.agreedBy, str, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, ],
        fee: typing.Union[MetaOapg.properties.fee, decimal.Decimal, int, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'ConsentRedemption':
        return super().__new__(
            cls,
            *args,
            agreedAt=agreedAt,
            agreedBy=agreedBy,
            price=price,
            fee=fee,
            currency=currency,
            _configuration=_configuration,
        )