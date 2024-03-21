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

from godaddy_python_sdk.model.consent import Consent as ConsentSchema
from godaddy_python_sdk.model.contact import Contact as ContactSchema
from godaddy_python_sdk.model.error import Error as ErrorSchema
from godaddy_python_sdk.model.domain_purchase_response import DomainPurchaseResponse as DomainPurchaseResponseSchema
from godaddy_python_sdk.model.domain_purchase import DomainPurchase as DomainPurchaseSchema
from godaddy_python_sdk.model.error_limit import ErrorLimit as ErrorLimitSchema

from godaddy_python_sdk.type.contact import Contact
from godaddy_python_sdk.type.domain_purchase_response import DomainPurchaseResponse
from godaddy_python_sdk.type.error import Error
from godaddy_python_sdk.type.domain_purchase import DomainPurchase
from godaddy_python_sdk.type.error_limit import ErrorLimit
from godaddy_python_sdk.type.consent import Consent

from ...api_client import Dictionary
from godaddy_python_sdk.pydantic.contact import Contact as ContactPydantic
from godaddy_python_sdk.pydantic.error_limit import ErrorLimit as ErrorLimitPydantic
from godaddy_python_sdk.pydantic.error import Error as ErrorPydantic
from godaddy_python_sdk.pydantic.domain_purchase import DomainPurchase as DomainPurchasePydantic
from godaddy_python_sdk.pydantic.consent import Consent as ConsentPydantic
from godaddy_python_sdk.pydantic.domain_purchase_response import DomainPurchaseResponse as DomainPurchaseResponsePydantic

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
# body param
SchemaForRequestBodyApplicationJson = DomainPurchaseSchema
SchemaForRequestBodyApplicationXml = DomainPurchaseSchema
SchemaForRequestBodyTextXml = DomainPurchaseSchema


request_body_domain_purchase = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaForRequestBodyTextXml),
    },
    required=True,
)
_auth = [
    'apiKey',
    'apiSecret',
]
SchemaFor200ResponseBodyApplicationJson = DomainPurchaseResponseSchema
SchemaFor200ResponseBodyApplicationJavascript = DomainPurchaseResponseSchema
SchemaFor200ResponseBodyApplicationXml = DomainPurchaseResponseSchema
SchemaFor200ResponseBodyTextJavascript = DomainPurchaseResponseSchema
SchemaFor200ResponseBodyTextXml = DomainPurchaseResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DomainPurchaseResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DomainPurchaseResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
    '429': _response_for_429,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'application/javascript',
    'application/xml',
    'text/javascript',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _create_domain_purchase_mapped_args(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if consent is not None:
            _body["consent"] = consent
        if contact_admin is not None:
            _body["contactAdmin"] = contact_admin
        if contact_billing is not None:
            _body["contactBilling"] = contact_billing
        if contact_registrant is not None:
            _body["contactRegistrant"] = contact_registrant
        if contact_tech is not None:
            _body["contactTech"] = contact_tech
        if domain is not None:
            _body["domain"] = domain
        if name_servers is not None:
            _body["nameServers"] = name_servers
        if period is not None:
            _body["period"] = period
        if privacy is not None:
            _body["privacy"] = privacy
        if renew_auto is not None:
            _body["renewAuto"] = renew_auto
        args.body = _body
        if x_shopper_id is not None:
            _header_params["X-Shopper-Id"] = x_shopper_id
        args.header = _header_params
        return args

    async def _acreate_domain_purchase_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Purchase and register the specified Domain
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
            path_template='/v1/domains/purchase',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_domain_purchase.serialize(body, content_type)
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


    def _create_domain_purchase_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Purchase and register the specified Domain
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
            path_template='/v1/domains/purchase',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_domain_purchase.serialize(body, content_type)
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


class CreateDomainPurchaseRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_domain_purchase(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_domain_purchase_mapped_args(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
        )
        return await self._acreate_domain_purchase_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_domain_purchase(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_domain_purchase_mapped_args(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
        )
        return self._create_domain_purchase_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateDomainPurchase(BaseApi):

    async def acreate_domain_purchase(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DomainPurchaseResponsePydantic:
        raw_response = await self.raw.acreate_domain_purchase(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
            **kwargs,
        )
        if validate:
            return DomainPurchaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DomainPurchaseResponsePydantic, raw_response.body)
    
    
    def create_domain_purchase(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DomainPurchaseResponsePydantic:
        raw_response = self.raw.create_domain_purchase(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
        )
        if validate:
            return DomainPurchaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DomainPurchaseResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_domain_purchase_mapped_args(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
        )
        return await self._acreate_domain_purchase_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        consent: Consent,
        domain: str,
        contact_admin: typing.Optional[Contact] = None,
        contact_billing: typing.Optional[Contact] = None,
        contact_registrant: typing.Optional[Contact] = None,
        contact_tech: typing.Optional[Contact] = None,
        name_servers: typing.Optional[typing.List[str]] = None,
        period: typing.Optional[int] = None,
        privacy: typing.Optional[bool] = None,
        renew_auto: typing.Optional[bool] = None,
        x_shopper_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_domain_purchase_mapped_args(
            body=body,
            consent=consent,
            domain=domain,
            contact_admin=contact_admin,
            contact_billing=contact_billing,
            contact_registrant=contact_registrant,
            contact_tech=contact_tech,
            name_servers=name_servers,
            period=period,
            privacy=privacy,
            renew_auto=renew_auto,
            x_shopper_id=x_shopper_id,
        )
        return self._create_domain_purchase_oapg(
            body=args.body,
            header_params=args.header,
        )

