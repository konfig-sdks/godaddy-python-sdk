<div align="left">

[![Visit Godaddy](./header.png)](https://developer.godaddy.com)

# Godaddy<a id="godaddy"></a>

All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`godaddy.actions.cancel_recent_action`](#godaddyactionscancel_recent_action)
  * [`godaddy.actions.get_recent_action`](#godaddyactionsget_recent_action)
  * [`godaddy.actions.get_recent_list`](#godaddyactionsget_recent_list)
  * [`godaddy.domains.accept_transfer_in`](#godaddydomainsaccept_transfer_in)
  * [`godaddy.domains.accept_transfer_out`](#godaddydomainsaccept_transfer_out)
  * [`godaddy.domains.cancel_forwarding_request`](#godaddydomainscancel_forwarding_request)
  * [`godaddy.domains.cancel_transfer_in`](#godaddydomainscancel_transfer_in)
  * [`godaddy.domains.create_forwarding_configuration`](#godaddydomainscreate_forwarding_configuration)
  * [`godaddy.domains.get_details`](#godaddydomainsget_details)
  * [`godaddy.domains.get_forwarding_info`](#godaddydomainsget_forwarding_info)
  * [`godaddy.domains.get_register_schema`](#godaddydomainsget_register_schema)
  * [`godaddy.domains.get_upcoming_maintenance_details`](#godaddydomainsget_upcoming_maintenance_details)
  * [`godaddy.domains.get_upcoming_maintenances_list`](#godaddydomainsget_upcoming_maintenances_list)
  * [`godaddy.domains.initiate_transfer_out`](#godaddydomainsinitiate_transfer_out)
  * [`godaddy.domains.modify_forwarding_info`](#godaddydomainsmodify_forwarding_info)
  * [`godaddy.domains.purchase_register_domain`](#godaddydomainspurchase_register_domain)
  * [`godaddy.domains.purchase_transfer_process`](#godaddydomainspurchase_transfer_process)
  * [`godaddy.domains.redeem_domain_restore`](#godaddydomainsredeem_domain_restore)
  * [`godaddy.domains.reject_transfer_out`](#godaddydomainsreject_transfer_out)
  * [`godaddy.domains.renew_domain`](#godaddydomainsrenew_domain)
  * [`godaddy.domains.restart_transfer_in`](#godaddydomainsrestart_transfer_in)
  * [`godaddy.domains.retry_transfer_in_process`](#godaddydomainsretry_transfer_in_process)
  * [`godaddy.domains.validate_domain_registration`](#godaddydomainsvalidate_domain_registration)
  * [`godaddy.notifications.acknowledge_domain_notification`](#godaddynotificationsacknowledge_domain_notification)
  * [`godaddy.notifications.get_next_domain`](#godaddynotificationsget_next_domain)
  * [`godaddy.notifications.get_schema`](#godaddynotificationsget_schema)
  * [`godaddy.notifications.list_opted_in_types`](#godaddynotificationslist_opted_in_types)
  * [`godaddy.notifications.opt_in_notifications`](#godaddynotificationsopt_in_notifications)
  * [`godaddy.v1.add_dns_records_to_domain`](#godaddyv1add_dns_records_to_domain)
  * [`godaddy.v1.cancel_domain_purchase`](#godaddyv1cancel_domain_purchase)
  * [`godaddy.v1.cancel_privacy_request`](#godaddyv1cancel_privacy_request)
  * [`godaddy.v1.check_domain_availability`](#godaddyv1check_domain_availability)
  * [`godaddy.v1.check_domain_availability_post`](#godaddyv1check_domain_availability_post)
  * [`godaddy.v1.create_domain_purchase`](#godaddyv1create_domain_purchase)
  * [`godaddy.v1.delete_all_dns_records`](#godaddyv1delete_all_dns_records)
  * [`godaddy.v1.get_dns_records`](#godaddyv1get_dns_records)
  * [`godaddy.v1.get_domain_details`](#godaddyv1get_domain_details)
  * [`godaddy.v1.get_domain_schema`](#godaddyv1get_domain_schema)
  * [`godaddy.v1.get_domains_list`](#godaddyv1get_domains_list)
  * [`godaddy.v1.get_legal_agreements`](#godaddyv1get_legal_agreements)
  * [`godaddy.v1.get_tlds_list`](#godaddyv1get_tlds_list)
  * [`godaddy.v1.purchase_privacy_for_domain`](#godaddyv1purchase_privacy_for_domain)
  * [`godaddy.v1.purchase_transfer_process`](#godaddyv1purchase_transfer_process)
  * [`godaddy.v1.renew_domain`](#godaddyv1renew_domain)
  * [`godaddy.v1.replace_dns_records`](#godaddyv1replace_dns_records)
  * [`godaddy.v1.replace_dns_records_type`](#godaddyv1replace_dns_records_type)
  * [`godaddy.v1.replace_dns_records_type_0`](#godaddyv1replace_dns_records_type_0)
  * [`godaddy.v1.resend_contact_email_verification`](#godaddyv1resend_contact_email_verification)
  * [`godaddy.v1.suggest_alternate_domains`](#godaddyv1suggest_alternate_domains)
  * [`godaddy.v1.update_domain_contacts`](#godaddyv1update_domain_contacts)
  * [`godaddy.v1.update_domain_details`](#godaddyv1update_domain_details)
  * [`godaddy.v1.validate_domain_contacts`](#godaddyv1validate_domain_contacts)
  * [`godaddy.v1.validate_domain_purchase`](#godaddyv1validate_domain_purchase)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=GoDaddy&serviceName=Domains&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from godaddy_python_sdk import GoDaddy, ApiException

godaddy = GoDaddy(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_KEY",
)

try:
    # Cancel the most recent user action for the specified domain
    godaddy.actions.cancel_recent_action(
        customer_id="customerId_example",
        domain="domain_example",
        type="AUTH_CODE_PURCHASE",
        x_request_id="string_example",
    )
except ApiException as e:
    print("Exception when calling ActionsApi.cancel_recent_action: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 429:
        pprint(e.body["code"])
        pprint(e.body["retry_after_sec"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 409:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from godaddy_python_sdk import GoDaddy, ApiException

godaddy = GoDaddy(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_KEY",
)


async def main():
    try:
        # Cancel the most recent user action for the specified domain
        await godaddy.actions.acancel_recent_action(
            customer_id="customerId_example",
            domain="domain_example",
            type="AUTH_CODE_PURCHASE",
            x_request_id="string_example",
        )
    except ApiException as e:
        print("Exception when calling ActionsApi.cancel_recent_action: %s\n" % e)
        pprint(e.body)
        if e.status == 401:
            pprint(e.body["code"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        if e.status == 500:
            pprint(e.body["code"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        if e.status == 403:
            pprint(e.body["code"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        if e.status == 404:
            pprint(e.body["code"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        if e.status == 429:
            pprint(e.body["code"])
            pprint(e.body["retry_after_sec"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        if e.status == 409:
            pprint(e.body["code"])
            pprint(e.body["fields"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from godaddy_python_sdk import GoDaddy, ApiException

godaddy = GoDaddy(
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_KEY",
)

try:
    # Cancel the most recent user action for the specified domain
    cancel_recent_action_response = godaddy.actions.raw.cancel_recent_action(
        customer_id="customerId_example",
        domain="domain_example",
        type="AUTH_CODE_PURCHASE",
        x_request_id="string_example",
    )
    pprint(cancel_recent_action_response.headers)
    pprint(cancel_recent_action_response.status)
    pprint(cancel_recent_action_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActionsApi.cancel_recent_action: %s\n" % e)
    pprint(e.body)
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 429:
        pprint(e.body["code"])
        pprint(e.body["retry_after_sec"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    if e.status == 409:
        pprint(e.body["code"])
        pprint(e.body["fields"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `godaddy.actions.cancel_recent_action`<a id="godaddyactionscancel_recent_action"></a>

Cancel the most recent user action for the specified domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.actions.cancel_recent_action(
    customer_id="customerId_example",
    domain="domain_example",
    type="AUTH_CODE_PURCHASE",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain whose action is to be cancelled

##### type: `str`<a id="type-str"></a>

The type of action to cancel

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/actions/{type}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.actions.get_recent_action`<a id="godaddyactionsget_recent_action"></a>

Retrieves the most recent action for the specified domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_action_response = godaddy.actions.get_recent_action(
    customer_id="customerId_example",
    domain="domain_example",
    type="AUTH_CODE_PURCHASE",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain whose action is to be retrieved

##### type: `str`<a id="type-str"></a>

The type of action to retrieve

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`Action`](./godaddy_python_sdk/pydantic/action.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/actions/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.actions.get_recent_list`<a id="godaddyactionsget_recent_list"></a>

Retrieves a list of the most recent actions for the specified domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_list_response = godaddy.actions.get_recent_list(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain whose actions are to be retrieved

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`ActionsGetRecentListResponse`](./godaddy_python_sdk/pydantic/actions_get_recent_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.accept_transfer_in`<a id="godaddydomainsaccept_transfer_in"></a>

Accepts the transfer in

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.accept_transfer_in(
    auth_code="string_example",
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_code: `str`<a id="auth_code-str"></a>

Authorization code for transferring the Domain

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to accept the transfer in for

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainTransferAuthCode`](./godaddy_python_sdk/type/domain_transfer_auth_code.py)
An Authorization code for transferring the Domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferInAccept` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.accept_transfer_out`<a id="godaddydomainsaccept_transfer_out"></a>

Accept transfer out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.accept_transfer_out(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to accept the transfer out for

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferOutAccept` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.cancel_forwarding_request`<a id="godaddydomainscancel_forwarding_request"></a>

<strong>Notes:</strong><ul><li>**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)</li></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.cancel_forwarding_request(
    customer_id="customerId_example",
    fqdn="fqdn_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### fqdn: `str`<a id="fqdn-str"></a>

The fully qualified domain name whose forwarding details are to be deleted.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/forwards/{fqdn}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.cancel_transfer_in`<a id="godaddydomainscancel_transfer_in"></a>

Cancels the transfer in

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.cancel_transfer_in(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to cancel the transfer in for

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferInCancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.create_forwarding_configuration`<a id="godaddydomainscreate_forwarding_configuration"></a>

<strong>Notes:</strong><ul><li>**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)</li></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.create_forwarding_configuration(
    body=None,
    type="REDIRECT_PERMANENT",
    url="string_example",
    customer_id="customerId_example",
    fqdn="fqdn_example",
    mask=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The type of fowarding to implement<br/><ul><li><strong style='margin-left: 12px;'>MASKED</strong> - Prevents the forwarded domain or subdomain URL from displaying in the browser's address bar.</li><li><strong style='margin-left: 12px;'>REDIRECT_PERMANENT*</strong> - Redirects to the url you specified in the forwardTo field using a `301 Moved Permanently` HTTP response. The HTTP 301 response code tells user-agents (including search engines) that the location has permanently moved.</li><li><strong style='margin-left: 12px;'>REDIRECT_TEMPORARY</strong> - Redirects to the url you specified in the forwardTo field using a `302 Found` HTTP response. The HTTP 302 response code tells user-agents (including search engines) that the location has temporarily moved.</li></ul>

##### url: `str`<a id="url-str"></a>

Forwards http(s) traffic to this destination url (ex. http://www.somedomain.com/)

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your own customer id.

##### fqdn: `str`<a id="fqdn-str"></a>

The fully qualified domain name whose forwarding details are to be modified.

##### mask: [`DomainForwardingMask`](./godaddy_python_sdk/type/domain_forwarding_mask.py)<a id="mask-domainforwardingmaskgodaddy_python_sdktypedomain_forwarding_maskpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainForwardingCreate`](./godaddy_python_sdk/type/domain_forwarding_create.py)
Domain forwarding rule to create for the specified fqdn

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/forwards/{fqdn}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.get_details`<a id="godaddydomainsget_details"></a>

Retrieve details for the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = godaddy.domains.get_details(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
    includes=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain name whose details are to be retrieved

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

##### includes: List[`str`]<a id="includes-liststr"></a>

Optional details to be included in the response

#### 🔄 Return<a id="🔄-return"></a>

[`DomainDetailV2`](./godaddy_python_sdk/pydantic/domain_detail_v2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.get_forwarding_info`<a id="godaddydomainsget_forwarding_info"></a>

<strong>Notes:</strong><ul><li>**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)</li></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_forwarding_info_response = godaddy.domains.get_forwarding_info(
    customer_id="customerId_example",
    fqdn="fqdn_example",
    include_subs=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### fqdn: `str`<a id="fqdn-str"></a>

The fully qualified domain name whose forwarding details are to be retrieved.

##### include_subs: `bool`<a id="include_subs-bool"></a>

Optionally include all sub domains if the fqdn specified is a domain and not a sub domain.

#### 🔄 Return<a id="🔄-return"></a>

[`DomainsGetForwardingInfoResponse`](./godaddy_python_sdk/pydantic/domains_get_forwarding_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/forwards/{fqdn}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.get_register_schema`<a id="godaddydomainsget_register_schema"></a>

Retrieve the schema to be submitted when registering a Domain for the specified TLD

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_register_schema_response = godaddy.domains.get_register_schema(
    customer_id="customerId_example",
    tld="tld_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### tld: `str`<a id="tld-str"></a>

The Top-Level Domain whose schema should be retrieved

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`JsonSchema`](./godaddy_python_sdk/pydantic/json_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/register/schema/{tld}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.get_upcoming_maintenance_details`<a id="godaddydomainsget_upcoming_maintenance_details"></a>

Retrieve the details for an upcoming system Maintenances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_upcoming_maintenance_details_response = (
    godaddy.domains.get_upcoming_maintenance_details(
        maintenance_id="maintenanceId_example",
        x_request_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### maintenance_id: `str`<a id="maintenance_id-str"></a>

The identifier for the system maintenance

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`MaintenanceDetail`](./godaddy_python_sdk/pydantic/maintenance_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/domains/maintenances/{maintenanceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.get_upcoming_maintenances_list`<a id="godaddydomainsget_upcoming_maintenances_list"></a>

Retrieve a list of upcoming system Maintenances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_upcoming_maintenances_list_response = (
    godaddy.domains.get_upcoming_maintenances_list(
        x_request_id="string_example",
        status="ACTIVE",
        modified_at_after="string_example",
        starts_at_after="string_example",
        limit=100,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

##### status: `str`<a id="status-str"></a>

Only include results with the selected `status` value.  Returns all results if omitted<br/><ul><li><strong style='margin-left: 12px;'>ACTIVE</strong> - The upcoming maintenance is active.</li><li><strong style='margin-left: 12px;'>CANCELLED</strong> - The upcoming maintenance has been cancelled.</li></ul>

##### modified_at_after: `str`<a id="modified_at_after-str"></a>

Only include results with `modifiedAt` after the supplied date

##### starts_at_after: `str`<a id="starts_at_after-str"></a>

Only include results with `startsAt` after the supplied date

##### limit: `int`<a id="limit-int"></a>

Maximum number of results to return

#### 🔄 Return<a id="🔄-return"></a>

[`Maintenance`](./godaddy_python_sdk/pydantic/maintenance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/domains/maintenances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.initiate_transfer_out`<a id="godaddydomainsinitiate_transfer_out"></a>

Initiate transfer out to another registrar for a .uk domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.initiate_transfer_out(
    customer_id="customerId_example",
    domain="domain_example",
    registrar="registrar_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to initiate the transfer out for

##### registrar: `str`<a id="registrar-str"></a>

Registrar tag to push transfer to

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferOut` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.modify_forwarding_info`<a id="godaddydomainsmodify_forwarding_info"></a>

<strong>Notes:</strong><ul><li>**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)</li></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.modify_forwarding_info(
    body=None,
    type="REDIRECT_PERMANENT",
    url="string_example",
    customer_id="customerId_example",
    fqdn="fqdn_example",
    mask=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The type of fowarding to implement<br/><ul><li><strong style='margin-left: 12px;'>MASKED</strong> - Prevents the forwarded domain or subdomain URL from displaying in the browser's address bar.</li><li><strong style='margin-left: 12px;'>REDIRECT_PERMANENT*</strong> - Redirects to the url you specified in the forwardTo field using a `301 Moved Permanently` HTTP response. The HTTP 301 response code tells user-agents (including search engines) that the location has permanently moved.</li><li><strong style='margin-left: 12px;'>REDIRECT_TEMPORARY</strong> - Redirects to the url you specified in the forwardTo field using a `302 Found` HTTP response. The HTTP 302 response code tells user-agents (including search engines) that the location has temporarily moved.</li></ul>

##### url: `str`<a id="url-str"></a>

Forwards http(s) traffic to this destination url (ex. http://www.somedomain.com/)

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### fqdn: `str`<a id="fqdn-str"></a>

The fully qualified domain name whose forwarding details are to be modified.

##### mask: [`DomainForwardingMask`](./godaddy_python_sdk/type/domain_forwarding_mask.py)<a id="mask-domainforwardingmaskgodaddy_python_sdktypedomain_forwarding_maskpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainForwardingCreate`](./godaddy_python_sdk/type/domain_forwarding_create.py)
Domain forwarding rule to create or replace on the fqdn

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/forwards/{fqdn}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.purchase_register_domain`<a id="godaddydomainspurchase_register_domain"></a>

Purchase and register the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.purchase_register_domain(
    consent={
        "agreed_at": "agreed_at_example",
        "agreed_by": "agreed_by_example",
        "agreement_keys": ["agreement_keys_example"],
        "currency": "USD",
        "price": 1,
    },
    domain='k$?x u&K}qz^sEC(lJ)=,jQ*&6`$cClu+k& &su[-l#6V+V6rEtCO?%28nxs"k8z(!\\6\\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~h',
    customer_id="customerId_example",
    contacts={},
    metadata={},
    name_servers=["string_example"],
    period=1,
    privacy=False,
    renew_auto=True,
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`ConsentV2`](./godaddy_python_sdk/type/consent_v2.py)<a id="consent-consentv2godaddy_python_sdktypeconsent_v2py"></a>


##### domain: `str`<a id="domain-str"></a>

For internationalized domain names with non-ascii characters, the domain name is converted to punycode before format and pattern validation rules are checked

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### contacts: [`DomainContactsCreateV2`](./godaddy_python_sdk/type/domain_contacts_create_v2.py)<a id="contacts-domaincontactscreatev2godaddy_python_sdktypedomain_contacts_create_v2py"></a>


##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The domain eligibility data fields as specified by GET /v2/customers/{customerId}/domains/register/schema/{tld}

##### name_servers: List[`str`]<a id="name_servers-liststr"></a>

##### period: `int`<a id="period-int"></a>

##### privacy: `bool`<a id="privacy-bool"></a>

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainPurchaseV2`](./godaddy_python_sdk/type/domain_purchase_v2.py)
An instance document expected to match the JSON schema returned by `./schema/{tld}`

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/register` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.purchase_transfer_process`<a id="godaddydomainspurchase_transfer_process"></a>

Purchase and start or restart transfer process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.purchase_transfer_process(
    auth_code="string_example",
    consent={
        "agreed_at": "agreed_at_example",
        "agreed_by": "agreed_by_example",
        "agreement_keys": ["agreement_keys_example"],
        "currency": "USD",
        "price": 1,
    },
    customer_id="customerId_example",
    domain="domain_example",
    contacts={},
    identity_document_id="string_example",
    metadata={},
    period=1,
    privacy=False,
    renew_auto=True,
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_code: `str`<a id="auth_code-str"></a>

Authorization code from registrar for transferring a domain

##### consent: [`ConsentV2`](./godaddy_python_sdk/type/consent_v2.py)<a id="consent-consentv2godaddy_python_sdktypeconsent_v2py"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to transfer in

##### contacts: [`DomainContactsCreateV2`](./godaddy_python_sdk/type/domain_contacts_create_v2.py)<a id="contacts-domaincontactscreatev2godaddy_python_sdktypedomain_contacts_create_v2py"></a>


##### identity_document_id: `str`<a id="identity_document_id-str"></a>

Unique identifier of the identify document that the user wants to associate with the domain being transferred in. This is required only if the gaining registry has a requirement for an approved identity document

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The domain eligibility data fields as specified by GET /v2/customers/{customerId}/domains/register/schema/{tld}

##### period: `int`<a id="period-int"></a>

Can be more than 1 but no more than 10 years total including current registration length

##### privacy: `bool`<a id="privacy-bool"></a>

Whether or not privacy has been requested

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

Whether or not the domain should be configured to automatically renew

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainTransferInV2`](./godaddy_python_sdk/type/domain_transfer_in_v2.py)
Details for domain transfer purchase

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transfer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.redeem_domain_restore`<a id="godaddydomainsredeem_domain_restore"></a>

Purchase a restore for the given domain to bring it out of redemption

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.redeem_domain_restore(
    consent={
        "agreed_at": "agreed_at_example",
        "agreed_by": "agreed_by_example",
        "currency": "USD",
        "fee": 1,
        "price": 1,
    },
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`ConsentRedemption`](./godaddy_python_sdk/type/consent_redemption.py)<a id="consent-consentredemptiongodaddy_python_sdktypeconsent_redemptionpy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to request redeem for

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainRedeemV2`](./godaddy_python_sdk/type/domain_redeem_v2.py)
Options for redeeming existing Domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/redeem` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.reject_transfer_out`<a id="godaddydomainsreject_transfer_out"></a>

Reject transfer out

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.reject_transfer_out(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
    reason="EVIDENCE_OF_FRAUD",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to reject the transfer out for

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

##### reason: `str`<a id="reason-str"></a>

Transfer out reject reason

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferOutReject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.renew_domain`<a id="godaddydomainsrenew_domain"></a>

Renew the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.renew_domain(
    consent={
        "agreed_at": "agreed_at_example",
        "agreed_by": "agreed_by_example",
        "currency": "USD",
        "price": 1,
    },
    expires="string_example",
    customer_id="customerId_example",
    domain="domain_example",
    period=1,
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`ConsentRenew`](./godaddy_python_sdk/type/consent_renew.py)<a id="consent-consentrenewgodaddy_python_sdktypeconsent_renewpy"></a>


##### expires: `str`<a id="expires-str"></a>

Current date when this domain will expire

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to be renewed

##### period: `int`<a id="period-int"></a>

Number of years to extend the Domain. Must not exceed maximum for TLD. When omitted, defaults to `period` specified during original purchase

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainRenewV2`](./godaddy_python_sdk/type/domain_renew_v2.py)
Options for renewing existing Domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/renew` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.restart_transfer_in`<a id="godaddydomainsrestart_transfer_in"></a>

Restarts transfer in request from the beginning

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.restart_transfer_in(
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to restart the transfer in

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferInRestart` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.retry_transfer_in_process`<a id="godaddydomainsretry_transfer_in_process"></a>

Retries the current transfer in request with supplied Authorization code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.retry_transfer_in_process(
    auth_code="string_example",
    customer_id="customerId_example",
    domain="domain_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_code: `str`<a id="auth_code-str"></a>

Authorization code for transferring the Domain

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### domain: `str`<a id="domain-str"></a>

Domain to retry the transfer in

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainTransferAuthCode`](./godaddy_python_sdk/type/domain_transfer_auth_code.py)
An Authorization code for transferring the Domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/{domain}/transferInRetry` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.domains.validate_domain_registration`<a id="godaddydomainsvalidate_domain_registration"></a>

Validate the request body using the Domain Registration Schema for the specified TLD

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.domains.validate_domain_registration(
    consent={
        "agreed_at": "agreed_at_example",
        "agreed_by": "agreed_by_example",
        "agreement_keys": ["agreement_keys_example"],
        "currency": "USD",
        "price": 1,
    },
    domain='k$?x u&K}qz^sEC(lJ)=,jQ*&6`$cClu+k& &su[-l#6V+V6rEtCO?%28nxs"k8z(!\\6\\$TMxo:,sWVoim9gsbE`buHkrTt{qxXp~h',
    customer_id="customerId_example",
    contacts={},
    metadata={},
    name_servers=["string_example"],
    period=1,
    privacy=False,
    renew_auto=True,
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`ConsentV2`](./godaddy_python_sdk/type/consent_v2.py)<a id="consent-consentv2godaddy_python_sdktypeconsent_v2py"></a>


##### domain: `str`<a id="domain-str"></a>

For internationalized domain names with non-ascii characters, the domain name is converted to punycode before format and pattern validation rules are checked

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### contacts: [`DomainContactsCreateV2`](./godaddy_python_sdk/type/domain_contacts_create_v2.py)<a id="contacts-domaincontactscreatev2godaddy_python_sdktypedomain_contacts_create_v2py"></a>


##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The domain eligibility data fields as specified by GET /v2/customers/{customerId}/domains/register/schema/{tld}

##### name_servers: List[`str`]<a id="name_servers-liststr"></a>

##### period: `int`<a id="period-int"></a>

##### privacy: `bool`<a id="privacy-bool"></a>

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainPurchaseV2`](./godaddy_python_sdk/type/domain_purchase_v2.py)
An instance document expected to match the JSON schema returned by `./schema/{tld}`

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/register/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.notifications.acknowledge_domain_notification`<a id="godaddynotificationsacknowledge_domain_notification"></a>

Acknowledge a domain notification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.notifications.acknowledge_domain_notification(
    customer_id="customerId_example",
    notification_id="notificationId_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### notification_id: `str`<a id="notification_id-str"></a>

The notification ID to acknowledge

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/notifications/{notificationId}/acknowledge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.notifications.get_next_domain`<a id="godaddynotificationsget_next_domain"></a>

Retrieve the next domain notification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_next_domain_response = godaddy.notifications.get_next_domain(
    customer_id="customerId_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`DomainNotification`](./godaddy_python_sdk/pydantic/domain_notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.notifications.get_schema`<a id="godaddynotificationsget_schema"></a>

Retrieve the schema for the notification data for the specified notification type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_schema_response = godaddy.notifications.get_schema(
    customer_id="customerId_example",
    type="AUTO_RENEWAL",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### type: `str`<a id="type-str"></a>

The notification type whose schema should be retrieved

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`JsonSchema`](./godaddy_python_sdk/pydantic/json_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/notifications/schemas/{type}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.notifications.list_opted_in_types`<a id="godaddynotificationslist_opted_in_types"></a>

Retrieve a list of notification types that are opted in

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_opted_in_types_response = godaddy.notifications.list_opted_in_types(
    customer_id="customerId_example",
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🔄 Return<a id="🔄-return"></a>

[`NotificationsListOptedInTypesResponse`](./godaddy_python_sdk/pydantic/notifications_list_opted_in_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/notifications/optIn` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.notifications.opt_in_notifications`<a id="godaddynotificationsopt_in_notifications"></a>

Opt in to recieve notifications for the submitted notification types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.notifications.opt_in_notifications(
    customer_id="customerId_example",
    types=["AUTH_CODE_PURCHASE"],
    x_request_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Customer identifier<br/> Note: For API Resellers, performing actions on behalf of your customers, you need to specify the Subaccount you're operating on behalf of; otherwise use your shopper id.

##### types: List[`str`]<a id="types-liststr"></a>

The notification types that should be opted in

##### x_request_id: `str`<a id="x_request_id-str"></a>

A client provided identifier for tracking this request.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/customers/{customerId}/domains/notifications/optIn` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.add_dns_records_to_domain`<a id="godaddyv1add_dns_records_to_domain"></a>

Add the specified DNS Records to the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.add_dns_records_to_domain(
    body=[None],
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be augmented

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

##### requestBody: [`ArrayOfDNSRecord`](./godaddy_python_sdk/type/array_of_dns_record.py)<a id="requestbody-arrayofdnsrecordgodaddy_python_sdktypearray_of_dns_recordpy"></a>

DNS Records to add to whatever currently exists

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.cancel_domain_purchase`<a id="godaddyv1cancel_domain_purchase"></a>

Cancel a purchased domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.cancel_domain_purchase(
    domain="domain_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain to cancel

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.cancel_privacy_request`<a id="godaddyv1cancel_privacy_request"></a>

Submit a privacy cancellation request for the given domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.cancel_privacy_request(
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose privacy is to be cancelled

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID of the owner of the domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/privacy` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.check_domain_availability`<a id="godaddyv1check_domain_availability"></a>

Determine whether or not the specified domain is available for purchase

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_domain_availability_response = godaddy.v1.check_domain_availability(
    domain="domain_example",
    check_type="FAST",
    for_transfer=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain name whose availability is to be checked

##### check_type: `str`<a id="check_type-str"></a>

Optimize for time ('FAST') or accuracy ('FULL')

##### for_transfer: `bool`<a id="for_transfer-bool"></a>

Whether or not to include domains available for transfer. If set to True, checkType is ignored

#### 🔄 Return<a id="🔄-return"></a>

[`DomainAvailableResponse`](./godaddy_python_sdk/pydantic/domain_available_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/available` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.check_domain_availability_post`<a id="godaddyv1check_domain_availability_post"></a>

Determine whether or not the specified domains are available for purchase

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_domain_availability_post_response = godaddy.v1.check_domain_availability_post(
    body=["v1_check_domain_availability_post_request_example"],
    check_type="FAST",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### check_type: `str`<a id="check_type-str"></a>

Optimize for time ('FAST') or accuracy ('FULL')

##### requestBody: [`V1CheckDomainAvailabilityPostRequest`](./godaddy_python_sdk/type/v1_check_domain_availability_post_request.py)<a id="requestbody-v1checkdomainavailabilitypostrequestgodaddy_python_sdktypev1_check_domain_availability_post_requestpy"></a>

Domain names for which to check availability

#### 🔄 Return<a id="🔄-return"></a>

[`DomainAvailableBulk`](./godaddy_python_sdk/pydantic/domain_available_bulk.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/available` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.create_domain_purchase`<a id="godaddyv1create_domain_purchase"></a>

Purchase and register the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_domain_purchase_response = godaddy.v1.create_domain_purchase(
    body=None,
    consent=None,
    domain="string_example",
    contact_admin=None,
    contact_billing=None,
    contact_registrant=None,
    contact_tech=None,
    name_servers=["string_example"],
    period=1,
    privacy=False,
    renew_auto=True,
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`Consent`](./godaddy_python_sdk/type/consent.py)<a id="consent-consentgodaddy_python_sdktypeconsentpy"></a>


##### domain: `str`<a id="domain-str"></a>

For internationalized domain names with non-ascii characters, the domain name is converted to punycode before format and pattern validation rules are checked

##### contact_admin: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_admin-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_billing: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_billing-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_registrant: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_registrant-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_tech: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_tech-contactgodaddy_python_sdktypecontactpy"></a>


##### name_servers: List[`str`]<a id="name_servers-liststr"></a>

##### period: `int`<a id="period-int"></a>

##### privacy: `bool`<a id="privacy-bool"></a>

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

The Shopper for whom the domain should be purchased

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainPurchase`](./godaddy_python_sdk/type/domain_purchase.py)
An instance document expected to match the JSON schema returned by `./schema/{tld}`

#### 🔄 Return<a id="🔄-return"></a>

[`DomainPurchaseResponse`](./godaddy_python_sdk/pydantic/domain_purchase_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/purchase` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.delete_all_dns_records`<a id="godaddyv1delete_all_dns_records"></a>

Delete all DNS Records for the specified Domain with the specified Type and Name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.delete_all_dns_records(
    domain="domain_example",
    type="A",
    name="name_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be deleted

##### type: `str`<a id="type-str"></a>

DNS Record Type for which DNS Records are to be deleted

##### name: `str`<a id="name-str"></a>

DNS Record Name for which DNS Records are to be deleted

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records/{type}/{name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_dns_records`<a id="godaddyv1get_dns_records"></a>

Retrieve DNS Records for the specified Domain, optionally with the specified Type and/or Name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dns_records_response = godaddy.v1.get_dns_records(
    domain="domain_example",
    type="A",
    name="name_example",
    x_shopper_id="string_example",
    offset=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be retrieved

##### type: `str`<a id="type-str"></a>

DNS Record Type for which DNS Records are to be retrieved

##### name: `str`<a id="name-str"></a>

DNS Record Name for which DNS Records are to be retrieved

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

##### offset: `int`<a id="offset-int"></a>

Number of results to skip for pagination

##### limit: `int`<a id="limit-int"></a>

Maximum number of items to return

#### 🔄 Return<a id="🔄-return"></a>

[`V1GetDnsRecords200Response`](./godaddy_python_sdk/pydantic/v1_get_dns_records200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records/{type}/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_domain_details`<a id="godaddyv1get_domain_details"></a>

Retrieve details for the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_domain_details_response = godaddy.v1.get_domain_details(
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain name whose details are to be retrieved

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID expected to own the specified domain

#### 🔄 Return<a id="🔄-return"></a>

[`DomainDetail`](./godaddy_python_sdk/pydantic/domain_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_domain_schema`<a id="godaddyv1get_domain_schema"></a>

Retrieve the schema to be submitted when registering a Domain for the specified TLD

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_domain_schema_response = godaddy.v1.get_domain_schema(
    tld="tld_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tld: `str`<a id="tld-str"></a>

The Top-Level Domain whose schema should be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`JsonSchema`](./godaddy_python_sdk/pydantic/json_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/purchase/schema/{tld}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_domains_list`<a id="godaddyv1get_domains_list"></a>

Retrieve a list of Domains for the specified Shopper

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_domains_list_response = godaddy.v1.get_domains_list(
    x_shopper_id="string_example",
    statuses=["string_example"],
    status_groups=["string_example"],
    limit=1,
    marker="string_example",
    includes=["string_example"],
    modified_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID whose domains are to be retrieved

##### statuses: List[`str`]<a id="statuses-liststr"></a>

Only include results with `status` value in the specified set

##### status_groups: List[`str`]<a id="status_groups-liststr"></a>

Only include results with `status` value in any of the specified groups

##### limit: `int`<a id="limit-int"></a>

Maximum number of domains to return

##### marker: `str`<a id="marker-str"></a>

Marker Domain to use as the offset in results

##### includes: List[`str`]<a id="includes-liststr"></a>

Optional details to be included in the response

##### modified_date: `str`<a id="modified_date-str"></a>

Only include results that have been modified since the specified date

#### 🔄 Return<a id="🔄-return"></a>

[`V1GetDomainsList200Response`](./godaddy_python_sdk/pydantic/v1_get_domains_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_legal_agreements`<a id="godaddyv1get_legal_agreements"></a>

Retrieve the legal agreement(s) required to purchase the specified TLD and add-ons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_legal_agreements_response = godaddy.v1.get_legal_agreements(
    tlds=["tlds_example"],
    privacy=True,
    x_market_id="en-US",
    for_transfer=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tlds: List[`str`]<a id="tlds-liststr"></a>

list of TLDs whose legal agreements are to be retrieved

##### privacy: `bool`<a id="privacy-bool"></a>

Whether or not privacy has been requested

##### x_market_id: `str`<a id="x_market_id-str"></a>

Unique identifier of the Market used to retrieve/translate Legal Agreements

##### for_transfer: `bool`<a id="for_transfer-bool"></a>

Whether or not domain tranfer has been requested

#### 🔄 Return<a id="🔄-return"></a>

[`V1GetLegalAgreements200Response`](./godaddy_python_sdk/pydantic/v1_get_legal_agreements200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/agreements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.get_tlds_list`<a id="godaddyv1get_tlds_list"></a>

Retrieves a list of TLDs supported and enabled for sale

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tlds_list_response = godaddy.v1.get_tlds_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`V1GetTldsList200Response`](./godaddy_python_sdk/pydantic/v1_get_tlds_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/tlds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.purchase_privacy_for_domain`<a id="godaddyv1purchase_privacy_for_domain"></a>

Purchase privacy for a specified domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
purchase_privacy_for_domain_response = godaddy.v1.purchase_privacy_for_domain(
    body=None,
    consent=None,
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`Consent`](./godaddy_python_sdk/type/consent.py)<a id="consent-consentgodaddy_python_sdktypeconsentpy"></a>


##### domain: `str`<a id="domain-str"></a>

Domain for which to purchase privacy

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID of the owner of the domain

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrivacyPurchase`](./godaddy_python_sdk/type/privacy_purchase.py)
Options for purchasing privacy

#### 🔄 Return<a id="🔄-return"></a>

[`DomainPurchaseResponse`](./godaddy_python_sdk/pydantic/domain_purchase_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/privacy/purchase` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.purchase_transfer_process`<a id="godaddyv1purchase_transfer_process"></a>

Purchase and start or restart transfer process

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
purchase_transfer_process_response = godaddy.v1.purchase_transfer_process(
    body=None,
    auth_code="string_example",
    consent=None,
    domain="domain_example",
    contact_admin=None,
    contact_billing=None,
    contact_registrant=None,
    contact_tech=None,
    period=1,
    privacy=False,
    renew_auto=True,
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auth_code: `str`<a id="auth_code-str"></a>

Authorization code from registrar for transferring a domain

##### consent: [`Consent`](./godaddy_python_sdk/type/consent.py)<a id="consent-consentgodaddy_python_sdktypeconsentpy"></a>


##### domain: `str`<a id="domain-str"></a>

Domain to transfer in

##### contact_admin: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_admin-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_billing: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_billing-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_registrant: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_registrant-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_tech: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_tech-contactgodaddy_python_sdktypecontactpy"></a>


##### period: `int`<a id="period-int"></a>

Can be more than 1 but no more than 10 years total including current registration length

##### privacy: `bool`<a id="privacy-bool"></a>

Whether or not privacy has been requested

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

Whether or not the domain should be configured to automatically renew

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

The Shopper to whom the domain should be transfered

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainTransferIn`](./godaddy_python_sdk/type/domain_transfer_in.py)
Details for domain transfer purchase

#### 🔄 Return<a id="🔄-return"></a>

[`DomainPurchaseResponse`](./godaddy_python_sdk/pydantic/domain_purchase_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/transfer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.renew_domain`<a id="godaddyv1renew_domain"></a>

Renew the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
renew_domain_response = godaddy.v1.renew_domain(
    body=None,
    domain="domain_example",
    period=1,
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain to renew

##### period: `int`<a id="period-int"></a>

Number of years to extend the Domain. Must not exceed maximum for TLD. When omitted, defaults to `period` specified during original purchase

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper for whom Domain is to be renewed. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainRenew`](./godaddy_python_sdk/type/domain_renew.py)
Options for renewing existing Domain

#### 🔄 Return<a id="🔄-return"></a>

[`DomainPurchaseResponse`](./godaddy_python_sdk/pydantic/domain_purchase_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/renew` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.replace_dns_records`<a id="godaddyv1replace_dns_records"></a>

Replace all DNS Records for the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.replace_dns_records(
    body=[None],
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be replaced

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

##### requestBody: [`V1ReplaceDnsRecordsRequest`](./godaddy_python_sdk/type/v1_replace_dns_records_request.py)<a id="requestbody-v1replacednsrecordsrequestgodaddy_python_sdktypev1_replace_dns_records_requestpy"></a>

DNS Records to replace whatever currently exists

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.replace_dns_records_type`<a id="godaddyv1replace_dns_records_type"></a>

Replace all DNS Records for the specified Domain with the specified Type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.replace_dns_records_type(
    body=[None],
    domain="domain_example",
    type="A",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be replaced

##### type: `str`<a id="type-str"></a>

DNS Record Type for which DNS Records are to be replaced

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

##### requestBody: [`V1ReplaceDnsRecordsTypeRequest`](./godaddy_python_sdk/type/v1_replace_dns_records_type_request.py)<a id="requestbody-v1replacednsrecordstyperequestgodaddy_python_sdktypev1_replace_dns_records_type_requestpy"></a>

DNS Records to replace whatever currently exists

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records/{type}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.replace_dns_records_type_0`<a id="godaddyv1replace_dns_records_type_0"></a>

Replace all DNS Records for the specified Domain with the specified Type and Name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.replace_dns_records_type_0(
    body=[None],
    domain="domain_example",
    type="A",
    name="name_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose DNS Records are to be replaced

##### type: `str`<a id="type-str"></a>

DNS Record Type for which DNS Records are to be replaced

##### name: `str`<a id="name-str"></a>

DNS Record Name for which DNS Records are to be replaced

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID which owns the domain. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

##### requestBody: [`V1ReplaceDnsRecordsTypeRequest3`](./godaddy_python_sdk/type/v1_replace_dns_records_type_request3.py)<a id="requestbody-v1replacednsrecordstyperequest3godaddy_python_sdktypev1_replace_dns_records_type_request3py"></a>

DNS Records to replace whatever currently exists

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/records/{type}/{name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.resend_contact_email_verification`<a id="godaddyv1resend_contact_email_verification"></a>

Re-send Contact E-mail Verification for specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.resend_contact_email_verification(
    domain="domain_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose Contact E-mail should be verified.

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper for whom domain contact e-mail should be verified. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/verifyRegistrantEmail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.suggest_alternate_domains`<a id="godaddyv1suggest_alternate_domains"></a>

Suggest alternate Domain names based on a seed Domain, a set of keywords, or the shopper's purchase history

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
suggest_alternate_domains_response = godaddy.v1.suggest_alternate_domains(
    x_shopper_id="string_example",
    query="string_example",
    country="AC",
    city="string_example",
    sources=["string_example"],
    tlds=["string_example"],
    length_max=1,
    length_min=1,
    limit=1,
    wait_ms=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper ID for which the suggestions are being generated

##### query: `str`<a id="query-str"></a>

Domain name or set of keywords for which alternative domain names will be suggested

##### country: `str`<a id="country-str"></a>

Two-letter ISO country code to be used as a hint for target region<br/><br/> NOTE: These are sample values, there are many <a href=\"http://www.iso.org/iso/country_codes.htm\">more</a>

##### city: `str`<a id="city-str"></a>

Name of city to be used as a hint for target region

##### sources: List[`str`]<a id="sources-liststr"></a>

Sources to be queried<br/><br/><ul> <li><strong>CC_TLD</strong> - Varies the TLD using Country Codes</li> <li><strong>EXTENSION</strong> - Varies the TLD</li> <li><strong>KEYWORD_SPIN</strong> - Identifies keywords and then rotates each one</li> <li><strong>PREMIUM</strong> - Includes variations with premium prices</li></ul>

##### tlds: List[`str`]<a id="tlds-liststr"></a>

Top-level domains to be included in suggestions<br/><br/> NOTE: These are sample values, there are many <a href=\"http://www.godaddy.com/tlds/gtld.aspx#domain_search_form\">more</a>

##### length_max: `int`<a id="length_max-int"></a>

Maximum length of second-level domain

##### length_min: `int`<a id="length_min-int"></a>

Minimum length of second-level domain

##### limit: `int`<a id="limit-int"></a>

Maximum number of suggestions to return

##### wait_ms: `int`<a id="wait_ms-int"></a>

Maximum amount of time, in milliseconds, to wait for responses If elapses, return the results compiled up to that point

#### 🔄 Return<a id="🔄-return"></a>

[`V1SuggestAlternateDomains200Response`](./godaddy_python_sdk/pydantic/v1_suggest_alternate_domains200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/suggest` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.update_domain_contacts`<a id="godaddyv1update_domain_contacts"></a>

Update domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.update_domain_contacts(
    body=None,
    contact_registrant=None,
    domain="domain_example",
    contact_admin=None,
    contact_billing=None,
    contact_tech=None,
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_registrant: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_registrant-contactgodaddy_python_sdktypecontactpy"></a>


##### domain: `str`<a id="domain-str"></a>

Domain whose Contacts are to be updated.

##### contact_admin: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_admin-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_billing: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_billing-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_tech: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_tech-contactgodaddy_python_sdktypecontactpy"></a>


##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper for whom domain contacts are to be updated. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainContacts`](./godaddy_python_sdk/type/domain_contacts.py)
Changes to apply to existing Contacts

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}/contacts` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.update_domain_details`<a id="godaddyv1update_domain_details"></a>

Update details for the specified Domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.update_domain_details(
    body=None,
    domain="domain_example",
    consent=None,
    expose_whois=True,
    locked=True,
    name_servers=[None],
    renew_auto=True,
    subaccount_id="string_example",
    x_shopper_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

Domain whose details are to be updated

##### consent: [`ConsentDomainUpdate`](./godaddy_python_sdk/type/consent_domain_update.py)<a id="consent-consentdomainupdategodaddy_python_sdktypeconsent_domain_updatepy"></a>


##### expose_whois: `bool`<a id="expose_whois-bool"></a>

Whether or not the domain contact details should be shown in the WHOIS

##### locked: `bool`<a id="locked-bool"></a>

Whether or not the domain should be locked to prevent transfers

##### name_servers: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./godaddy_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="name_servers-listunionbool-date-datetime-dict-float-int-list-str-nonegodaddy_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Fully-qualified domain names for Name Servers to associate with the domain

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

Whether or not the domain should be configured to automatically renew

##### subaccount_id: `str`<a id="subaccount_id-str"></a>

Reseller subaccount shopperid who can manage the domain

##### x_shopper_id: `str`<a id="x_shopper_id-str"></a>

Shopper for whom Domain is to be updated. NOTE: This is only required if you are a Reseller managing a domain purchased outside the scope of your reseller account. For instance, if you're a Reseller, but purchased a Domain via http://www.godaddy.com

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainUpdate`](./godaddy_python_sdk/type/domain_update.py)
Changes to apply to existing Domain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/{domain}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.validate_domain_contacts`<a id="godaddyv1validate_domain_contacts"></a>

All contacts specified in request will be validated against all domains specifed in "domains". As an alternative, you can also pass in tlds, with the exception of `uk`, which requires full domain names

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.validate_domain_contacts(
    body=None,
    domains=["string_example"],
    contact_admin=None,
    contact_billing=None,
    contact_presence=None,
    contact_registrant=None,
    contact_tech=None,
    entity_type="ABORIGINAL",
    x_private_label_id=1,
    market_id="en-US",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domains: List[`str`]<a id="domains-liststr"></a>

An array of domain names to be validated against. Alternatively, you can specify the extracted tlds. However, full domain names are required if the tld is `uk`

##### contact_admin: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_admin-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_billing: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_billing-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_presence: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_presence-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_registrant: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_registrant-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_tech: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_tech-contactgodaddy_python_sdktypecontactpy"></a>


##### entity_type: `str`<a id="entity_type-str"></a>

Canadian Presence Requirement (CA)

##### x_private_label_id: `int`<a id="x_private_label_id-int"></a>

PrivateLabelId to operate as, if different from JWT

##### market_id: `str`<a id="market_id-str"></a>

MarketId in which the request is being made, and for which responses should be localized

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainsContactsBulk`](./godaddy_python_sdk/type/domains_contacts_bulk.py)
An instance document expected for domains contacts validation

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/contacts/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `godaddy.v1.validate_domain_purchase`<a id="godaddyv1validate_domain_purchase"></a>

Validate the request body using the Domain Purchase Schema for the specified TLD

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
godaddy.v1.validate_domain_purchase(
    body=None,
    consent=None,
    domain="string_example",
    contact_admin=None,
    contact_billing=None,
    contact_registrant=None,
    contact_tech=None,
    name_servers=["string_example"],
    period=1,
    privacy=False,
    renew_auto=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent: [`Consent`](./godaddy_python_sdk/type/consent.py)<a id="consent-consentgodaddy_python_sdktypeconsentpy"></a>


##### domain: `str`<a id="domain-str"></a>

For internationalized domain names with non-ascii characters, the domain name is converted to punycode before format and pattern validation rules are checked

##### contact_admin: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_admin-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_billing: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_billing-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_registrant: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_registrant-contactgodaddy_python_sdktypecontactpy"></a>


##### contact_tech: [`Contact`](./godaddy_python_sdk/type/contact.py)<a id="contact_tech-contactgodaddy_python_sdktypecontactpy"></a>


##### name_servers: List[`str`]<a id="name_servers-liststr"></a>

##### period: `int`<a id="period-int"></a>

##### privacy: `bool`<a id="privacy-bool"></a>

##### renew_auto: `bool`<a id="renew_auto-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainPurchase`](./godaddy_python_sdk/type/domain_purchase.py)
An instance document expected to match the JSON schema returned by `./schema/{tld}`

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/domains/purchase/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
