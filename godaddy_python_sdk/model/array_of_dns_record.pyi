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


class ArrayOfDNSRecord(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['DNSRecord']:
            return DNSRecord

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['DNSRecord'], typing.List['DNSRecord']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ArrayOfDNSRecord':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'DNSRecord':
        return super().__getitem__(i)

from godaddy_python_sdk.model.dns_record import DNSRecord
