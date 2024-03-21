# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from godaddy_python_sdk.paths.v1_domains_domain_records.patch import AddDnsRecordsToDomain
from godaddy_python_sdk.paths.v1_domains_domain.delete import CancelDomainPurchase
from godaddy_python_sdk.paths.v1_domains_domain_privacy.delete import CancelPrivacyRequest
from godaddy_python_sdk.paths.v1_domains_available.get import CheckDomainAvailability
from godaddy_python_sdk.paths.v1_domains_available.post import CheckDomainAvailabilityPost
from godaddy_python_sdk.paths.v1_domains_purchase.post import CreateDomainPurchase
from godaddy_python_sdk.paths.v1_domains_domain_records_type_name.delete import DeleteAllDnsRecords
from godaddy_python_sdk.paths.v1_domains_domain_records_type_name.get import GetDnsRecords
from godaddy_python_sdk.paths.v1_domains_domain.get import GetDomainDetails
from godaddy_python_sdk.paths.v1_domains_purchase_schema_tld.get import GetDomainSchema
from godaddy_python_sdk.paths.v1_domains.get import GetDomainsList
from godaddy_python_sdk.paths.v1_domains_agreements.get import GetLegalAgreements
from godaddy_python_sdk.paths.v1_domains_tlds.get import GetTldsList
from godaddy_python_sdk.paths.v1_domains_domain_privacy_purchase.post import PurchasePrivacyForDomain
from godaddy_python_sdk.paths.v1_domains_domain_transfer.post import PurchaseTransferProcess
from godaddy_python_sdk.paths.v1_domains_domain_renew.post import RenewDomain
from godaddy_python_sdk.paths.v1_domains_domain_records.put import ReplaceDnsRecords
from godaddy_python_sdk.paths.v1_domains_domain_records_type.put import ReplaceDnsRecordsType
from godaddy_python_sdk.paths.v1_domains_domain_records_type_name.put import ReplaceDnsRecordsType0
from godaddy_python_sdk.paths.v1_domains_domain_verify_registrant_email.post import ResendContactEmailVerification
from godaddy_python_sdk.paths.v1_domains_suggest.get import SuggestAlternateDomains
from godaddy_python_sdk.paths.v1_domains_domain_contacts.patch import UpdateDomainContacts
from godaddy_python_sdk.paths.v1_domains_domain.patch import UpdateDomainDetails
from godaddy_python_sdk.paths.v1_domains_contacts_validate.post import ValidateDomainContacts
from godaddy_python_sdk.paths.v1_domains_purchase_validate.post import ValidateDomainPurchase
from godaddy_python_sdk.apis.tags.v1_api_raw import V1ApiRaw


class V1Api(
    AddDnsRecordsToDomain,
    CancelDomainPurchase,
    CancelPrivacyRequest,
    CheckDomainAvailability,
    CheckDomainAvailabilityPost,
    CreateDomainPurchase,
    DeleteAllDnsRecords,
    GetDnsRecords,
    GetDomainDetails,
    GetDomainSchema,
    GetDomainsList,
    GetLegalAgreements,
    GetTldsList,
    PurchasePrivacyForDomain,
    PurchaseTransferProcess,
    RenewDomain,
    ReplaceDnsRecords,
    ReplaceDnsRecordsType,
    ReplaceDnsRecordsType0,
    ResendContactEmailVerification,
    SuggestAlternateDomains,
    UpdateDomainContacts,
    UpdateDomainDetails,
    ValidateDomainContacts,
    ValidateDomainPurchase,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: V1ApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = V1ApiRaw(api_client)
