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

# Query params


class ReasonSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def EVIDENCE_OF_FRAUD(cls):
        return cls("EVIDENCE_OF_FRAUD")
    
    @schemas.classproperty
    def URDP_ACTION(cls):
        return cls("URDP_ACTION")
    
    @schemas.classproperty
    def COURT_ORDER(cls):
        return cls("COURT_ORDER")
    
    @schemas.classproperty
    def DISPUTE_OVER_IDENTITY(cls):
        return cls("DISPUTE_OVER_IDENTITY")
    
    @schemas.classproperty
    def NO_PAYMENT_FOR_PREVIOUS_REGISTRATION_PERIOD(cls):
        return cls("NO_PAYMENT_FOR_PREVIOUS_REGISTRATION_PERIOD")
    
    @schemas.classproperty
    def WRITTEN_OBJECTION(cls):
        return cls("WRITTEN_OBJECTION")
    
    @schemas.classproperty
    def TRANSFERRED_WITHIN_SIXTY_DAYS(cls):
        return cls("TRANSFERRED_WITHIN_SIXTY_DAYS")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'reason': typing.Union[ReasonSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_reason = api_client.QueryParameter(
    name="reason",
    style=api_client.ParameterStyle.FORM,
    schema=ReasonSchema,
    explode=True,
)
# Header params
XRequestIdSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Request-Id': typing.Union[XRequestIdSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_request_id = api_client.HeaderParameter(
    name="X-Request-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIdSchema,
)
# Path params
CustomerIdSchema = schemas.StrSchema
DomainSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'customerId': typing.Union[CustomerIdSchema, str, ],
        'domain': typing.Union[DomainSchema, str, ],
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
request_path_domain = api_client.PathParameter(
    name="domain",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DomainSchema,
    required=True,
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _reject_transfer_out_mapped_args(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if reason is not None:
            _query_params["reason"] = reason
        if x_request_id is not None:
            _header_params["X-Request-Id"] = x_request_id
        if customer_id is not None:
            _path_params["customerId"] = customer_id
        if domain is not None:
            _path_params["domain"] = domain
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _areject_transfer_out_oapg(
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
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Reject transfer out
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
            request_path_customer_id,
            request_path_domain,
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
            request_query_reason,
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
            request_header_x_request_id,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/customers/{customerId}/domains/{domain}/transferOutReject',
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


    def _reject_transfer_out_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Reject transfer out
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
            request_path_customer_id,
            request_path_domain,
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
            request_query_reason,
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
            request_header_x_request_id,
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
        method = 'post'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/customers/{customerId}/domains/{domain}/transferOutReject',
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


class RejectTransferOutRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def areject_transfer_out(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._reject_transfer_out_mapped_args(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
        )
        return await self._areject_transfer_out_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def reject_transfer_out(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._reject_transfer_out_mapped_args(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
        )
        return self._reject_transfer_out_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class RejectTransferOut(BaseApi):

    async def areject_transfer_out(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.areject_transfer_out(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
            **kwargs,
        )
    
    
    def reject_transfer_out(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.reject_transfer_out(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._reject_transfer_out_mapped_args(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
        )
        return await self._areject_transfer_out_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        customer_id: str,
        domain: str,
        x_request_id: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._reject_transfer_out_mapped_args(
            customer_id=customer_id,
            domain=domain,
            x_request_id=x_request_id,
            reason=reason,
        )
        return self._reject_transfer_out_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

