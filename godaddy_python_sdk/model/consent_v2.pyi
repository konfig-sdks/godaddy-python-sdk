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


class ConsentV2(
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
            "currency",
            "agreementKeys",
        }
        
        class properties:
            agreedAt = schemas.StrSchema
            agreedBy = schemas.StrSchema
            
            
            class agreementKeys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
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
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
            price = schemas.IntSchema
            claimToken = schemas.StrSchema
            registryPremiumPricing = schemas.BoolSchema
            __annotations__ = {
                "agreedAt": agreedAt,
                "agreedBy": agreedBy,
                "agreementKeys": agreementKeys,
                "currency": currency,
                "price": price,
                "claimToken": claimToken,
                "registryPremiumPricing": registryPremiumPricing,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    agreedAt: MetaOapg.properties.agreedAt
    agreedBy: MetaOapg.properties.agreedBy
    price: MetaOapg.properties.price
    currency: MetaOapg.properties.currency
    agreementKeys: MetaOapg.properties.agreementKeys
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreementKeys"]) -> MetaOapg.properties.agreementKeys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["claimToken"]) -> MetaOapg.properties.claimToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registryPremiumPricing"]) -> MetaOapg.properties.registryPremiumPricing: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agreedAt"], typing_extensions.Literal["agreedBy"], typing_extensions.Literal["price"], typing_extensions.Literal["currency"], typing_extensions.Literal["agreementKeys"], typing_extensions.Literal["claimToken"], typing_extensions.Literal["registryPremiumPricing"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedAt"]) -> MetaOapg.properties.agreedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreedBy"]) -> MetaOapg.properties.agreedBy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreementKeys"]) -> MetaOapg.properties.agreementKeys: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["claimToken"]) -> typing.Union[MetaOapg.properties.claimToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registryPremiumPricing"]) -> typing.Union[MetaOapg.properties.registryPremiumPricing, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agreedAt"], typing_extensions.Literal["agreedBy"], typing_extensions.Literal["price"], typing_extensions.Literal["currency"], typing_extensions.Literal["agreementKeys"], typing_extensions.Literal["claimToken"], typing_extensions.Literal["registryPremiumPricing"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agreedAt: typing.Union[MetaOapg.properties.agreedAt, str, ],
        agreedBy: typing.Union[MetaOapg.properties.agreedBy, str, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        agreementKeys: typing.Union[MetaOapg.properties.agreementKeys, list, tuple, ],
        claimToken: typing.Union[MetaOapg.properties.claimToken, str, schemas.Unset] = schemas.unset,
        registryPremiumPricing: typing.Union[MetaOapg.properties.registryPremiumPricing, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'ConsentV2':
        return super().__new__(
            cls,
            *args,
            agreedAt=agreedAt,
            agreedBy=agreedBy,
            price=price,
            currency=currency,
            agreementKeys=agreementKeys,
            claimToken=claimToken,
            registryPremiumPricing=registryPremiumPricing,
            _configuration=_configuration,
        )
