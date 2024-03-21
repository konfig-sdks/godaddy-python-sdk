# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from godaddy_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from godaddy_python_sdk.api_response import AsyncGeneratorResponse
from godaddy_python_sdk import api_client, exceptions
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

from godaddy_python_sdk.model.error import Error as ErrorSchema
from godaddy_python_sdk.model.error_limit import ErrorLimit as ErrorLimitSchema

from godaddy_python_sdk.type.error import Error
from godaddy_python_sdk.type.error_limit import ErrorLimit

from ...api_client import Dictionary
from godaddy_python_sdk.pydantic.error_limit import ErrorLimit as ErrorLimitPydantic
from godaddy_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# Header params
XShopperIdSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Shopper-Id': typing.Union[XShopperIdSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_shopper_id = api_client.HeaderParameter(
    name="X-Shopper-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XShopperIdSchema,
)
# Path params
DomainSchema = schemas.StrSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "A": "A",
            "AAAA": "AAAA",
            "CNAME": "CNAME",
            "MX": "MX",
            "SRV": "SRV",
            "TXT": "TXT",
        }
    
    @schemas.classproperty
    def A(cls):
        return cls("A")
    
    @schemas.classproperty
    def AAAA(cls):
        return cls("AAAA")
    
    @schemas.classproperty
    def CNAME(cls):
        return cls("CNAME")
    
    @schemas.classproperty
    def MX(cls):
        return cls("MX")
    
    @schemas.classproperty
    def SRV(cls):
        return cls("SRV")
    
    @schemas.classproperty
    def TXT(cls):
        return cls("TXT")
NameSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'domain': typing.Union[DomainSchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
        'name': typing.Union[NameSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_domain = api_client.PathParameter(
    name="domain",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DomainSchema,
    required=True,
)
request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
request_path_name = api_client.PathParameter(
    name="name",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NameSchema,
    required=True,
)
_auth = [
    'apiKey',
    'apiSecret',
]


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
SchemaFor400ResponseBodyApplicationJson = ErrorSchema
SchemaFor400ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor400ResponseBodyApplicationXml = ErrorSchema
SchemaFor400ResponseBodyTextJavascript = ErrorSchema
SchemaFor400ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextXml),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorSchema
SchemaFor401ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor401ResponseBodyApplicationXml = ErrorSchema
SchemaFor401ResponseBodyTextJavascript = ErrorSchema
SchemaFor401ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: Error


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextXml),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorSchema
SchemaFor403ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor403ResponseBodyApplicationXml = ErrorSchema
SchemaFor403ResponseBodyTextJavascript = ErrorSchema
SchemaFor403ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Error


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor403ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor403ResponseBodyTextXml),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorSchema
SchemaFor404ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor404ResponseBodyApplicationXml = ErrorSchema
SchemaFor404ResponseBodyTextJavascript = ErrorSchema
SchemaFor404ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextXml),
    },
)
SchemaFor409ResponseBodyApplicationJson = ErrorSchema
SchemaFor409ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor409ResponseBodyApplicationXml = ErrorSchema
SchemaFor409ResponseBodyTextJavascript = ErrorSchema
SchemaFor409ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: Error


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor409ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor409ResponseBodyTextXml),
    },
)
SchemaFor422ResponseBodyApplicationJson = ErrorSchema
SchemaFor422ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor422ResponseBodyApplicationXml = ErrorSchema
SchemaFor422ResponseBodyTextJavascript = ErrorSchema
SchemaFor422ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: Error


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor422ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor422ResponseBodyTextXml),
    },
)
SchemaFor429ResponseBodyApplicationJson = ErrorLimitSchema
SchemaFor429ResponseBodyApplicationJavascript = ErrorLimitSchema
SchemaFor429ResponseBodyApplicationXml = ErrorLimitSchema
SchemaFor429ResponseBodyTextJavascript = ErrorLimitSchema
SchemaFor429ResponseBodyTextXml = ErrorLimitSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: ErrorLimit


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: ErrorLimit


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor429ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor429ResponseBodyTextXml),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorSchema
SchemaFor500ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor500ResponseBodyApplicationXml = ErrorSchema
SchemaFor500ResponseBodyTextJavascript = ErrorSchema
SchemaFor500ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Error


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextXml),
    },
)
SchemaFor504ResponseBodyApplicationJson = ErrorSchema
SchemaFor504ResponseBodyApplicationJavascript = ErrorSchema
SchemaFor504ResponseBodyApplicationXml = ErrorSchema
SchemaFor504ResponseBodyTextJavascript = ErrorSchema
SchemaFor504ResponseBodyTextXml = ErrorSchema


@dataclass
class ApiResponseFor504(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor504Async(api_client.AsyncApiResponse):
    body: Error


_response_for_504 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor504,
    response_cls_async=ApiResponseFor504Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor504ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor504ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor504ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor504ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor504ResponseBodyTextXml),
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '409': _response_for_409,
    '422': _response_for_422,
    '429': _response_for_429,
    '500': _response_for_500,
    '504': _response_for_504,
}
_all_accept_content_types = (
    'application/json',
    'application/javascript',
    'application/xml',
    'text/javascript',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _delete_all_dns_records_mapped_args(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        if x_shopper_id is not None:
            _header_params["X-Shopper-Id"] = x_shopper_id
        if domain is not None:
            _path_params["domain"] = domain
        if type is not None:
            _path_params["type"] = type
        if name is not None:
            _path_params["name"] = name
        args.header = _header_params
        args.path = _path_params
        return args

    async def _adelete_all_dns_records_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Delete all DNS Records for the specified Domain with the specified Type and Name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_domain,
            request_path_type,
            request_path_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_shopper_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/domains/{domain}/records/{type}/{name}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _delete_all_dns_records_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Delete all DNS Records for the specified Domain with the specified Type and Name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_domain,
            request_path_type,
            request_path_name,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_shopper_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/domains/{domain}/records/{type}/{name}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class DeleteAllDnsRecordsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adelete_all_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_all_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
        )
        return await self._adelete_all_dns_records_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def delete_all_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_all_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
        )
        return self._delete_all_dns_records_oapg(
            header_params=args.header,
            path_params=args.path,
        )

class DeleteAllDnsRecords(BaseApi):

    async def adelete_all_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.adelete_all_dns_records(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            **kwargs,
        )
    
    
    def delete_all_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.delete_all_dns_records(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_all_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
        )
        return await self._adelete_all_dns_records_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_all_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
        )
        return self._delete_all_dns_records_oapg(
            header_params=args.header,
            path_params=args.path,
        )

