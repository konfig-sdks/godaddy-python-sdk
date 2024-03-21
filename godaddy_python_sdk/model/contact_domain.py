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


class ContactDomain(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "nameLast",
            "nameFirst",
            "addressMailing",
            "phone",
            "email",
            "exposeWhois",
        }
        
        class properties:
        
            @staticmethod
            def addressMailing() -> typing.Type['Address']:
                return Address
            
            
            class email(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'email'
                    max_length = 80
            exposeWhois = schemas.BoolSchema
            
            
            class nameFirst(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'person-name'
                    max_length = 30
            
            
            class nameLast(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'person-name'
                    max_length = 30
            
            
            class phone(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'phone'
                    max_length = 17
            _createdAt = schemas.StrSchema
            _deleted = schemas.BoolSchema
            _modifiedAt = schemas.StrSchema
            _revision = schemas.IntSchema
            contactId = schemas.StrSchema
            
            
            class encoding(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ASCII": "ASCII",
                        "UTF-8": "UTF8",
                    }
                
                @schemas.classproperty
                def ASCII(cls):
                    return cls("ASCII")
                
                @schemas.classproperty
                def UTF8(cls):
                    return cls("UTF-8")
            
            
            class fax(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'phone'
                    max_length = 17
            jobTitle = schemas.StrSchema
            metadata = schemas.DictSchema
            nameMiddle = schemas.StrSchema
            
            
            class organization(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'organization-name'
                    max_length = 100
            
            
            class tlds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tlds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "addressMailing": addressMailing,
                "email": email,
                "exposeWhois": exposeWhois,
                "nameFirst": nameFirst,
                "nameLast": nameLast,
                "phone": phone,
                "_createdAt": _createdAt,
                "_deleted": _deleted,
                "_modifiedAt": _modifiedAt,
                "_revision": _revision,
                "contactId": contactId,
                "encoding": encoding,
                "fax": fax,
                "jobTitle": jobTitle,
                "metadata": metadata,
                "nameMiddle": nameMiddle,
                "organization": organization,
                "tlds": tlds,
            }

    
    nameLast: MetaOapg.properties.nameLast
    nameFirst: MetaOapg.properties.nameFirst
    addressMailing: 'Address'
    phone: MetaOapg.properties.phone
    email: MetaOapg.properties.email
    exposeWhois: MetaOapg.properties.exposeWhois
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressMailing"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exposeWhois"]) -> MetaOapg.properties.exposeWhois: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameFirst"]) -> MetaOapg.properties.nameFirst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameLast"]) -> MetaOapg.properties.nameLast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_createdAt"]) -> MetaOapg.properties._createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_deleted"]) -> MetaOapg.properties._deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_modifiedAt"]) -> MetaOapg.properties._modifiedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_revision"]) -> MetaOapg.properties._revision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encoding"]) -> MetaOapg.properties.encoding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fax"]) -> MetaOapg.properties.fax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobTitle"]) -> MetaOapg.properties.jobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameMiddle"]) -> MetaOapg.properties.nameMiddle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tlds"]) -> MetaOapg.properties.tlds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressMailing", "email", "exposeWhois", "nameFirst", "nameLast", "phone", "_createdAt", "_deleted", "_modifiedAt", "_revision", "contactId", "encoding", "fax", "jobTitle", "metadata", "nameMiddle", "organization", "tlds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressMailing"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exposeWhois"]) -> MetaOapg.properties.exposeWhois: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameFirst"]) -> MetaOapg.properties.nameFirst: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameLast"]) -> MetaOapg.properties.nameLast: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_createdAt"]) -> typing.Union[MetaOapg.properties._createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_deleted"]) -> typing.Union[MetaOapg.properties._deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_modifiedAt"]) -> typing.Union[MetaOapg.properties._modifiedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_revision"]) -> typing.Union[MetaOapg.properties._revision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encoding"]) -> typing.Union[MetaOapg.properties.encoding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fax"]) -> typing.Union[MetaOapg.properties.fax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobTitle"]) -> typing.Union[MetaOapg.properties.jobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameMiddle"]) -> typing.Union[MetaOapg.properties.nameMiddle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tlds"]) -> typing.Union[MetaOapg.properties.tlds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressMailing", "email", "exposeWhois", "nameFirst", "nameLast", "phone", "_createdAt", "_deleted", "_modifiedAt", "_revision", "contactId", "encoding", "fax", "jobTitle", "metadata", "nameMiddle", "organization", "tlds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        nameLast: typing.Union[MetaOapg.properties.nameLast, str, ],
        nameFirst: typing.Union[MetaOapg.properties.nameFirst, str, ],
        addressMailing: 'Address',
        phone: typing.Union[MetaOapg.properties.phone, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        exposeWhois: typing.Union[MetaOapg.properties.exposeWhois, bool, ],
        _createdAt: typing.Union[MetaOapg.properties._createdAt, str, schemas.Unset] = schemas.unset,
        _deleted: typing.Union[MetaOapg.properties._deleted, bool, schemas.Unset] = schemas.unset,
        _modifiedAt: typing.Union[MetaOapg.properties._modifiedAt, str, schemas.Unset] = schemas.unset,
        _revision: typing.Union[MetaOapg.properties._revision, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, str, schemas.Unset] = schemas.unset,
        encoding: typing.Union[MetaOapg.properties.encoding, str, schemas.Unset] = schemas.unset,
        fax: typing.Union[MetaOapg.properties.fax, str, schemas.Unset] = schemas.unset,
        jobTitle: typing.Union[MetaOapg.properties.jobTitle, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        nameMiddle: typing.Union[MetaOapg.properties.nameMiddle, str, schemas.Unset] = schemas.unset,
        organization: typing.Union[MetaOapg.properties.organization, str, schemas.Unset] = schemas.unset,
        tlds: typing.Union[MetaOapg.properties.tlds, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactDomain':
        return super().__new__(
            cls,
            *args,
            nameLast=nameLast,
            nameFirst=nameFirst,
            addressMailing=addressMailing,
            phone=phone,
            email=email,
            exposeWhois=exposeWhois,
            _createdAt=_createdAt,
            _deleted=_deleted,
            _modifiedAt=_modifiedAt,
            _revision=_revision,
            contactId=contactId,
            encoding=encoding,
            fax=fax,
            jobTitle=jobTitle,
            metadata=metadata,
            nameMiddle=nameMiddle,
            organization=organization,
            tlds=tlds,
            _configuration=_configuration,
            **kwargs,
        )

from godaddy_python_sdk.model.address import Address
