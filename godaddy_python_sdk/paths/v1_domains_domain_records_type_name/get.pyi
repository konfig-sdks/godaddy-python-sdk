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
from godaddy_python_sdk.model.v1_get_dns_records_response import V1GetDnsRecordsResponse as V1GetDnsRecordsResponseSchema
from godaddy_python_sdk.model.v1_get_dns_records200_response2 import V1GetDnsRecords200Response2 as V1GetDnsRecords200Response2Schema
from godaddy_python_sdk.model.v1_get_dns_records200_response import V1GetDnsRecords200Response as V1GetDnsRecords200ResponseSchema
from godaddy_python_sdk.model.v1_get_dns_records200_response3 import V1GetDnsRecords200Response3 as V1GetDnsRecords200Response3Schema
from godaddy_python_sdk.model.v1_get_dns_records200_response1 import V1GetDnsRecords200Response1 as V1GetDnsRecords200Response1Schema
from godaddy_python_sdk.model.error_limit import ErrorLimit as ErrorLimitSchema

from godaddy_python_sdk.type.v1_get_dns_records200_response1 import V1GetDnsRecords200Response1
from godaddy_python_sdk.type.v1_get_dns_records_response import V1GetDnsRecordsResponse
from godaddy_python_sdk.type.v1_get_dns_records200_response2 import V1GetDnsRecords200Response2
from godaddy_python_sdk.type.v1_get_dns_records200_response import V1GetDnsRecords200Response
from godaddy_python_sdk.type.error import Error
from godaddy_python_sdk.type.error_limit import ErrorLimit
from godaddy_python_sdk.type.v1_get_dns_records200_response3 import V1GetDnsRecords200Response3

from ...api_client import Dictionary
from godaddy_python_sdk.pydantic.v1_get_dns_records200_response import V1GetDnsRecords200Response as V1GetDnsRecords200ResponsePydantic
from godaddy_python_sdk.pydantic.error_limit import ErrorLimit as ErrorLimitPydantic
from godaddy_python_sdk.pydantic.error import Error as ErrorPydantic
from godaddy_python_sdk.pydantic.v1_get_dns_records_response import V1GetDnsRecordsResponse as V1GetDnsRecordsResponsePydantic
from godaddy_python_sdk.pydantic.v1_get_dns_records200_response3 import V1GetDnsRecords200Response3 as V1GetDnsRecords200Response3Pydantic
from godaddy_python_sdk.pydantic.v1_get_dns_records200_response2 import V1GetDnsRecords200Response2 as V1GetDnsRecords200Response2Pydantic
from godaddy_python_sdk.pydantic.v1_get_dns_records200_response1 import V1GetDnsRecords200Response1 as V1GetDnsRecords200Response1Pydantic

# Query params
OffsetSchema = schemas.IntSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
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
    def NS(cls):
        return cls("NS")
    
    @schemas.classproperty
    def SOA(cls):
        return cls("SOA")
    
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
SchemaFor200ResponseBodyApplicationJson = V1GetDnsRecords200ResponseSchema
SchemaFor200ResponseBodyApplicationJavascript = V1GetDnsRecordsResponseSchema
SchemaFor200ResponseBodyApplicationXml = V1GetDnsRecords200Response1Schema
SchemaFor200ResponseBodyTextJavascript = V1GetDnsRecords200Response2Schema
SchemaFor200ResponseBodyTextXml = V1GetDnsRecords200Response3Schema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: V1GetDnsRecords200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: V1GetDnsRecords200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/javascript': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJavascript),
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
        'text/javascript': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJavascript),
        'text/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextXml),
    },
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
_all_accept_content_types = (
    'application/json',
    'application/javascript',
    'application/xml',
    'text/javascript',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _get_dns_records_mapped_args(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if offset is not None:
            _query_params["offset"] = offset
        if limit is not None:
            _query_params["limit"] = limit
        if x_shopper_id is not None:
            _header_params["X-Shopper-Id"] = x_shopper_id
        if domain is not None:
            _path_params["domain"] = domain
        if type is not None:
            _path_params["type"] = type
        if name is not None:
            _path_params["name"] = name
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_dns_records_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve DNS Records for the specified Domain, optionally with the specified Type and/or Name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_dns_records_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve DNS Records for the specified Domain, optionally with the specified Type and/or Name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_offset,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
        method = 'get'.upper()
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetDnsRecordsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
        )
        return await self._aget_dns_records_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
        )
        return self._get_dns_records_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class GetDnsRecords(BaseApi):

    async def aget_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> V1GetDnsRecords200ResponsePydantic:
        raw_response = await self.raw.aget_dns_records(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
            **kwargs,
        )
        if validate:
            return RootModel[V1GetDnsRecords200ResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(V1GetDnsRecords200ResponsePydantic, raw_response.body)
    
    
    def get_dns_records(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> V1GetDnsRecords200ResponsePydantic:
        raw_response = self.raw.get_dns_records(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
        )
        if validate:
            return RootModel[V1GetDnsRecords200ResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(V1GetDnsRecords200ResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
        )
        return await self._aget_dns_records_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        domain: str,
        type: str,
        name: str,
        x_shopper_id: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_dns_records_mapped_args(
            domain=domain,
            type=type,
            name=name,
            x_shopper_id=x_shopper_id,
            offset=offset,
            limit=limit,
        )
        return self._get_dns_records_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )
