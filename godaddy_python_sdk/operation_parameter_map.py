operation_parameter_map = {
    '/v2/customers/{customerId}/domains/{domain}/actions/{type}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/actions/{type}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/actions-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferInAccept-POST': {
        'parameters': [
            {
                'name': 'authCode'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferOutAccept-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/forwards/{fqdn}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'fqdn'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferInCancel-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/forwards/{fqdn}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'url'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'fqdn'
            },
            {
                'name': 'mask'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
            {
                'name': 'includes'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/forwards/{fqdn}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'fqdn'
            },
            {
                'name': 'includeSubs'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/register/schema/{tld}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'tld'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/domains/maintenances/{maintenanceId}-GET': {
        'parameters': [
            {
                'name': 'maintenanceId'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/domains/maintenances-GET': {
        'parameters': [
            {
                'name': 'X-Request-Id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'modifiedAtAfter'
            },
            {
                'name': 'startsAtAfter'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferOut-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'registrar'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/forwards/{fqdn}-PUT': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'url'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'fqdn'
            },
            {
                'name': 'mask'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/register-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'nameServers'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transfer-POST': {
        'parameters': [
            {
                'name': 'authCode'
            },
            {
                'name': 'consent'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'identityDocumentId'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/redeem-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferOutReject-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/renew-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'expires'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'period'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferInRestart-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/{domain}/transferInRetry-POST': {
        'parameters': [
            {
                'name': 'authCode'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/register/validate-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'nameServers'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/notifications/{notificationId}/acknowledge-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'notificationId'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/notifications-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/notifications/schemas/{type}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/notifications/optIn-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v2/customers/{customerId}/domains/notifications/optIn-PUT': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'types'
            },
            {
                'name': 'X-Request-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records-PATCH': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}-DELETE': {
        'parameters': [
            {
                'name': 'domain'
            },
        ]
    },
    '/v1/domains/{domain}/privacy-DELETE': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/available-GET': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'checkType'
            },
            {
                'name': 'forTransfer'
            },
        ]
    },
    '/v1/domains/available-POST': {
        'parameters': [
            {
                'name': 'checkType'
            },
        ]
    },
    '/v1/domains/purchase-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'contactAdmin'
            },
            {
                'name': 'contactBilling'
            },
            {
                'name': 'contactRegistrant'
            },
            {
                'name': 'contactTech'
            },
            {
                'name': 'nameServers'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records/{type}/{name}-DELETE': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'name'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records/{type}/{name}-GET': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'name'
            },
            {
                'name': 'X-Shopper-Id'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/domains/{domain}-GET': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/purchase/schema/{tld}-GET': {
        'parameters': [
            {
                'name': 'tld'
            },
        ]
    },
    '/v1/domains-GET': {
        'parameters': [
            {
                'name': 'X-Shopper-Id'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'statusGroups'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'includes'
            },
            {
                'name': 'modifiedDate'
            },
        ]
    },
    '/v1/domains/agreements-GET': {
        'parameters': [
            {
                'name': 'tlds'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'X-Market-Id'
            },
            {
                'name': 'forTransfer'
            },
        ]
    },
    '/v1/domains/tlds-GET': {
        'parameters': [
        ]
    },
    '/v1/domains/{domain}/privacy/purchase-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/transfer-POST': {
        'parameters': [
            {
                'name': 'authCode'
            },
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'contactAdmin'
            },
            {
                'name': 'contactBilling'
            },
            {
                'name': 'contactRegistrant'
            },
            {
                'name': 'contactTech'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/renew-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'period'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records-PUT': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records/{type}-PUT': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/records/{type}/{name}-PUT': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'type'
            },
            {
                'name': 'name'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}/verifyRegistrantEmail-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/suggest-GET': {
        'parameters': [
            {
                'name': 'X-Shopper-Id'
            },
            {
                'name': 'query'
            },
            {
                'name': 'country'
            },
            {
                'name': 'city'
            },
            {
                'name': 'sources'
            },
            {
                'name': 'tlds'
            },
            {
                'name': 'lengthMax'
            },
            {
                'name': 'lengthMin'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'waitMs'
            },
        ]
    },
    '/v1/domains/{domain}/contacts-PATCH': {
        'parameters': [
            {
                'name': 'contactRegistrant'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'contactAdmin'
            },
            {
                'name': 'contactBilling'
            },
            {
                'name': 'contactTech'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/{domain}-PATCH': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'consent'
            },
            {
                'name': 'exposeWhois'
            },
            {
                'name': 'locked'
            },
            {
                'name': 'nameServers'
            },
            {
                'name': 'renewAuto'
            },
            {
                'name': 'subaccountId'
            },
            {
                'name': 'X-Shopper-Id'
            },
        ]
    },
    '/v1/domains/contacts/validate-POST': {
        'parameters': [
            {
                'name': 'domains'
            },
            {
                'name': 'contactAdmin'
            },
            {
                'name': 'contactBilling'
            },
            {
                'name': 'contactPresence'
            },
            {
                'name': 'contactRegistrant'
            },
            {
                'name': 'contactTech'
            },
            {
                'name': 'entityType'
            },
            {
                'name': 'X-Private-Label-Id'
            },
            {
                'name': 'marketId'
            },
        ]
    },
    '/v1/domains/purchase/validate-POST': {
        'parameters': [
            {
                'name': 'consent'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'contactAdmin'
            },
            {
                'name': 'contactBilling'
            },
            {
                'name': 'contactRegistrant'
            },
            {
                'name': 'contactTech'
            },
            {
                'name': 'nameServers'
            },
            {
                'name': 'period'
            },
            {
                'name': 'privacy'
            },
            {
                'name': 'renewAuto'
            },
        ]
    },
};