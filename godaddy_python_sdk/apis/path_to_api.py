import typing_extensions

from godaddy_python_sdk.paths import PathValues
from godaddy_python_sdk.apis.paths.v1_domains import V1Domains
from godaddy_python_sdk.apis.paths.v1_domains_agreements import V1DomainsAgreements
from godaddy_python_sdk.apis.paths.v1_domains_available import V1DomainsAvailable
from godaddy_python_sdk.apis.paths.v1_domains_contacts_validate import V1DomainsContactsValidate
from godaddy_python_sdk.apis.paths.v1_domains_purchase import V1DomainsPurchase
from godaddy_python_sdk.apis.paths.v1_domains_purchase_schema_tld import V1DomainsPurchaseSchemaTld
from godaddy_python_sdk.apis.paths.v1_domains_purchase_validate import V1DomainsPurchaseValidate
from godaddy_python_sdk.apis.paths.v1_domains_suggest import V1DomainsSuggest
from godaddy_python_sdk.apis.paths.v1_domains_tlds import V1DomainsTlds
from godaddy_python_sdk.apis.paths.v1_domains_domain import V1DomainsDomain
from godaddy_python_sdk.apis.paths.v1_domains_domain_contacts import V1DomainsDomainContacts
from godaddy_python_sdk.apis.paths.v1_domains_domain_privacy import V1DomainsDomainPrivacy
from godaddy_python_sdk.apis.paths.v1_domains_domain_privacy_purchase import V1DomainsDomainPrivacyPurchase
from godaddy_python_sdk.apis.paths.v1_domains_domain_records import V1DomainsDomainRecords
from godaddy_python_sdk.apis.paths.v1_domains_domain_records_type import V1DomainsDomainRecordsType
from godaddy_python_sdk.apis.paths.v1_domains_domain_records_type_name import V1DomainsDomainRecordsTypeName
from godaddy_python_sdk.apis.paths.v1_domains_domain_renew import V1DomainsDomainRenew
from godaddy_python_sdk.apis.paths.v1_domains_domain_transfer import V1DomainsDomainTransfer
from godaddy_python_sdk.apis.paths.v1_domains_domain_verify_registrant_email import V1DomainsDomainVerifyRegistrantEmail
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_forwards_fqdn import V2CustomersCustomerIdDomainsForwardsFqdn
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_notifications import V2CustomersCustomerIdDomainsNotifications
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_notifications_opt_in import V2CustomersCustomerIdDomainsNotificationsOptIn
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_notifications_schemas_type import V2CustomersCustomerIdDomainsNotificationsSchemasType
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_notifications_notification_id_acknowledge import V2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledge
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_register import V2CustomersCustomerIdDomainsRegister
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_register_schema_tld import V2CustomersCustomerIdDomainsRegisterSchemaTld
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_register_validate import V2CustomersCustomerIdDomainsRegisterValidate
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain import V2CustomersCustomerIdDomainsDomain
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_actions import V2CustomersCustomerIdDomainsDomainActions
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_actions_type import V2CustomersCustomerIdDomainsDomainActionsType
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_redeem import V2CustomersCustomerIdDomainsDomainRedeem
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_renew import V2CustomersCustomerIdDomainsDomainRenew
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer import V2CustomersCustomerIdDomainsDomainTransfer
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_in_accept import V2CustomersCustomerIdDomainsDomainTransferInAccept
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_in_cancel import V2CustomersCustomerIdDomainsDomainTransferInCancel
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_in_restart import V2CustomersCustomerIdDomainsDomainTransferInRestart
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_in_retry import V2CustomersCustomerIdDomainsDomainTransferInRetry
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_out import V2CustomersCustomerIdDomainsDomainTransferOut
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_out_accept import V2CustomersCustomerIdDomainsDomainTransferOutAccept
from godaddy_python_sdk.apis.paths.v2_customers_customer_id_domains_domain_transfer_out_reject import V2CustomersCustomerIdDomainsDomainTransferOutReject
from godaddy_python_sdk.apis.paths.v2_domains_maintenances import V2DomainsMaintenances
from godaddy_python_sdk.apis.paths.v2_domains_maintenances_maintenance_id import V2DomainsMaintenancesMaintenanceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_DOMAINS: V1Domains,
        PathValues.V1_DOMAINS_AGREEMENTS: V1DomainsAgreements,
        PathValues.V1_DOMAINS_AVAILABLE: V1DomainsAvailable,
        PathValues.V1_DOMAINS_CONTACTS_VALIDATE: V1DomainsContactsValidate,
        PathValues.V1_DOMAINS_PURCHASE: V1DomainsPurchase,
        PathValues.V1_DOMAINS_PURCHASE_SCHEMA_TLD: V1DomainsPurchaseSchemaTld,
        PathValues.V1_DOMAINS_PURCHASE_VALIDATE: V1DomainsPurchaseValidate,
        PathValues.V1_DOMAINS_SUGGEST: V1DomainsSuggest,
        PathValues.V1_DOMAINS_TLDS: V1DomainsTlds,
        PathValues.V1_DOMAINS_DOMAIN: V1DomainsDomain,
        PathValues.V1_DOMAINS_DOMAIN_CONTACTS: V1DomainsDomainContacts,
        PathValues.V1_DOMAINS_DOMAIN_PRIVACY: V1DomainsDomainPrivacy,
        PathValues.V1_DOMAINS_DOMAIN_PRIVACY_PURCHASE: V1DomainsDomainPrivacyPurchase,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS: V1DomainsDomainRecords,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS_TYPE: V1DomainsDomainRecordsType,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS_TYPE_NAME: V1DomainsDomainRecordsTypeName,
        PathValues.V1_DOMAINS_DOMAIN_RENEW: V1DomainsDomainRenew,
        PathValues.V1_DOMAINS_DOMAIN_TRANSFER: V1DomainsDomainTransfer,
        PathValues.V1_DOMAINS_DOMAIN_VERIFY_REGISTRANT_EMAIL: V1DomainsDomainVerifyRegistrantEmail,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_FORWARDS_FQDN: V2CustomersCustomerIdDomainsForwardsFqdn,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS: V2CustomersCustomerIdDomainsNotifications,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_OPT_IN: V2CustomersCustomerIdDomainsNotificationsOptIn,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_SCHEMAS_TYPE: V2CustomersCustomerIdDomainsNotificationsSchemasType,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_NOTIFICATION_ID_ACKNOWLEDGE: V2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledge,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER: V2CustomersCustomerIdDomainsRegister,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER_SCHEMA_TLD: V2CustomersCustomerIdDomainsRegisterSchemaTld,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER_VALIDATE: V2CustomersCustomerIdDomainsRegisterValidate,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN: V2CustomersCustomerIdDomainsDomain,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_ACTIONS: V2CustomersCustomerIdDomainsDomainActions,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_ACTIONS_TYPE: V2CustomersCustomerIdDomainsDomainActionsType,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_REDEEM: V2CustomersCustomerIdDomainsDomainRedeem,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_RENEW: V2CustomersCustomerIdDomainsDomainRenew,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER: V2CustomersCustomerIdDomainsDomainTransfer,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_ACCEPT: V2CustomersCustomerIdDomainsDomainTransferInAccept,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_CANCEL: V2CustomersCustomerIdDomainsDomainTransferInCancel,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_RESTART: V2CustomersCustomerIdDomainsDomainTransferInRestart,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_RETRY: V2CustomersCustomerIdDomainsDomainTransferInRetry,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT: V2CustomersCustomerIdDomainsDomainTransferOut,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT_ACCEPT: V2CustomersCustomerIdDomainsDomainTransferOutAccept,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT_REJECT: V2CustomersCustomerIdDomainsDomainTransferOutReject,
        PathValues.V2_DOMAINS_MAINTENANCES: V2DomainsMaintenances,
        PathValues.V2_DOMAINS_MAINTENANCES_MAINTENANCE_ID: V2DomainsMaintenancesMaintenanceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_DOMAINS: V1Domains,
        PathValues.V1_DOMAINS_AGREEMENTS: V1DomainsAgreements,
        PathValues.V1_DOMAINS_AVAILABLE: V1DomainsAvailable,
        PathValues.V1_DOMAINS_CONTACTS_VALIDATE: V1DomainsContactsValidate,
        PathValues.V1_DOMAINS_PURCHASE: V1DomainsPurchase,
        PathValues.V1_DOMAINS_PURCHASE_SCHEMA_TLD: V1DomainsPurchaseSchemaTld,
        PathValues.V1_DOMAINS_PURCHASE_VALIDATE: V1DomainsPurchaseValidate,
        PathValues.V1_DOMAINS_SUGGEST: V1DomainsSuggest,
        PathValues.V1_DOMAINS_TLDS: V1DomainsTlds,
        PathValues.V1_DOMAINS_DOMAIN: V1DomainsDomain,
        PathValues.V1_DOMAINS_DOMAIN_CONTACTS: V1DomainsDomainContacts,
        PathValues.V1_DOMAINS_DOMAIN_PRIVACY: V1DomainsDomainPrivacy,
        PathValues.V1_DOMAINS_DOMAIN_PRIVACY_PURCHASE: V1DomainsDomainPrivacyPurchase,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS: V1DomainsDomainRecords,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS_TYPE: V1DomainsDomainRecordsType,
        PathValues.V1_DOMAINS_DOMAIN_RECORDS_TYPE_NAME: V1DomainsDomainRecordsTypeName,
        PathValues.V1_DOMAINS_DOMAIN_RENEW: V1DomainsDomainRenew,
        PathValues.V1_DOMAINS_DOMAIN_TRANSFER: V1DomainsDomainTransfer,
        PathValues.V1_DOMAINS_DOMAIN_VERIFY_REGISTRANT_EMAIL: V1DomainsDomainVerifyRegistrantEmail,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_FORWARDS_FQDN: V2CustomersCustomerIdDomainsForwardsFqdn,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS: V2CustomersCustomerIdDomainsNotifications,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_OPT_IN: V2CustomersCustomerIdDomainsNotificationsOptIn,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_SCHEMAS_TYPE: V2CustomersCustomerIdDomainsNotificationsSchemasType,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_NOTIFICATIONS_NOTIFICATION_ID_ACKNOWLEDGE: V2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledge,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER: V2CustomersCustomerIdDomainsRegister,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER_SCHEMA_TLD: V2CustomersCustomerIdDomainsRegisterSchemaTld,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_REGISTER_VALIDATE: V2CustomersCustomerIdDomainsRegisterValidate,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN: V2CustomersCustomerIdDomainsDomain,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_ACTIONS: V2CustomersCustomerIdDomainsDomainActions,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_ACTIONS_TYPE: V2CustomersCustomerIdDomainsDomainActionsType,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_REDEEM: V2CustomersCustomerIdDomainsDomainRedeem,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_RENEW: V2CustomersCustomerIdDomainsDomainRenew,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER: V2CustomersCustomerIdDomainsDomainTransfer,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_ACCEPT: V2CustomersCustomerIdDomainsDomainTransferInAccept,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_CANCEL: V2CustomersCustomerIdDomainsDomainTransferInCancel,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_RESTART: V2CustomersCustomerIdDomainsDomainTransferInRestart,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_IN_RETRY: V2CustomersCustomerIdDomainsDomainTransferInRetry,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT: V2CustomersCustomerIdDomainsDomainTransferOut,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT_ACCEPT: V2CustomersCustomerIdDomainsDomainTransferOutAccept,
        PathValues.V2_CUSTOMERS_CUSTOMER_ID_DOMAINS_DOMAIN_TRANSFER_OUT_REJECT: V2CustomersCustomerIdDomainsDomainTransferOutReject,
        PathValues.V2_DOMAINS_MAINTENANCES: V2DomainsMaintenances,
        PathValues.V2_DOMAINS_MAINTENANCES_MAINTENANCE_ID: V2DomainsMaintenancesMaintenanceId,
    }
)
