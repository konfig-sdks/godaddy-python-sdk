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

from godaddy_python_sdk.model.domain_forwarding_mask import DomainForwardingMask as DomainForwardingMaskSchema
from godaddy_python_sdk.model.error import Error as ErrorSchema
from godaddy_python_sdk.model.domain_forwarding_create import DomainForwardingCreate as DomainForwardingCreateSchema
from godaddy_python_sdk.model.error_limit import ErrorLimit as ErrorLimitSchema

from godaddy_python_sdk.type.error import Error
from godaddy_python_sdk.type.domain_forwarding_mask import DomainForwardingMask
from godaddy_python_sdk.type.error_limit import ErrorLimit
from godaddy_python_sdk.type.domain_forwarding_create import DomainForwardingCreate

from ...api_client import Dictionary
from godaddy_python_sdk.pydantic.error_limit import ErrorLimit as ErrorLimitPydantic
from godaddy_python_sdk.pydantic.domain_forwarding_mask import DomainForwardingMask as DomainForwardingMaskPydantic
from godaddy_python_sdk.pydantic.error import Error as ErrorPydantic
from godaddy_python_sdk.pydantic.domain_forwarding_create import DomainForwardingCreate as DomainForwardingCreatePydantic

from . import path

# Path params
CustomerIdSchema = schemas.StrSchema
FqdnSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'customerId': typing.Union[CustomerIdSchema, str, ],
        'fqdn': typing.Union[FqdnSchema, str, ],
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


request_path_customer_id = api_client.PathParameter(
    name="customerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CustomerIdSchema,
    required=True,
)
request_path_fqdn = api_client.PathParameter(
    name="fqdn",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FqdnSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = DomainForwardingCreateSchema


request_body_domain_forwarding_create = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
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
SchemaFor401ResponseBodyApplicationJson = ErrorSchema


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
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorSchema


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
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorSchema


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
    },
)
SchemaFor409ResponseBodyApplicationJson = ErrorSchema


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
    },
)
SchemaFor422ResponseBodyApplicationJson = ErrorSchema


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
    },
)
SchemaFor429ResponseBodyApplicationJson = ErrorLimitSchema


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
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorSchema


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
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '409': _response_for_409,
    '422': _response_for_422,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_forwarding_configuration_mapped_args(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if mask is not None:
            _body["mask"] = mask
        if type is not None:
            _body["type"] = type
        if url is not None:
            _body["url"] = url
        args.body = _body
        if customer_id is not None:
            _path_params["customerId"] = customer_id
        if fqdn is not None:
            _path_params["fqdn"] = fqdn
        args.path = _path_params
        return args

    async def _acreate_forwarding_configuration_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new forwarding configuration for the given FQDN
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
            request_path_fqdn,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/customers/{customerId}/domains/forwards/{fqdn}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_domain_forwarding_create.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _create_forwarding_configuration_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new forwarding configuration for the given FQDN
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
            request_path_fqdn,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/customers/{customerId}/domains/forwards/{fqdn}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_domain_forwarding_create.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class CreateForwardingConfigurationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_forwarding_configuration(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_forwarding_configuration_mapped_args(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
        )
        return await self._acreate_forwarding_configuration_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_forwarding_configuration(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_forwarding_configuration_mapped_args(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
        )
        return self._create_forwarding_configuration_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateForwardingConfiguration(BaseApi):

    async def acreate_forwarding_configuration(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_forwarding_configuration(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
            **kwargs,
        )
    
    
    def create_forwarding_configuration(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_forwarding_configuration(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_forwarding_configuration_mapped_args(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
        )
        return await self._acreate_forwarding_configuration_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        type: str,
        url: str,
        customer_id: str,
        fqdn: str,
        mask: typing.Optional[DomainForwardingMask] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_forwarding_configuration_mapped_args(
            body=body,
            type=type,
            url=url,
            customer_id=customer_id,
            fqdn=fqdn,
            mask=mask,
        )
        return self._create_forwarding_configuration_oapg(
            body=args.body,
            path_params=args.path,
        )

