# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class DomainNotificationType(BaseModel):
    # The notification type
    type: Literal["AUTH_CODE_PURCHASE", "AUTH_CODE_REGENERATE", "AUTO_RENEWAL", "BACKORDER", "BACKORDER_PURCHASE", "BACKORDER_DELETE", "BACKORDER_UPDATE", "CONTACT_CREATE", "CONTACT_DELETE", "CONTACT_UPDATE", "DNS_VERIFICATION", "DNSSEC_CREATE", "DNSSEC_DELETE", "DOMAIN_DELETE", "DOMAIN_UPDATE", "DOMAIN_UPDATE_CONTACTS", "DOMAIN_UPDATE_NAME_SERVERS", "EXPIRY", "HOST_CREATE", "HOST_DELETE", "ICANN_VERIFICATION", "MIGRATE", "MIGRATE_IN", "PREMIUM", "PRIVACY_PURCHASE", "PRIVACY_DELETE", "REDEEM", "REGISTER", "RENEW", "RENEW_UNDO", "TRADE", "TRADE_CANCEL", "TRADE_PURCHASE", "TRADE_PURCHASE_AUTH_TEXT_MESSAGE", "TRADE_RESEND_AUTH_EMAIL", "TRANSFER", "TRANSFER_IN", "TRANSFER_IN_ACCEPT", "TRANSFER_IN_CANCEL", "TRANSFER_IN_RESTART", "TRANSFER_IN_RETRY", "TRANSFER_OUT", "TRANSFER_OUT_ACCEPT", "TRANSFER_OUT_REJECT", "TRANSFER_OUT_REQUESTED", "TRANSIT"] = Field(alias='type')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
