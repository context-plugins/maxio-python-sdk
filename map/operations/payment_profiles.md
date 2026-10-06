<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentProfiles — operations

Accessor: `client.payment_profiles` · Source: `maxio/apis/payment_profiles.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.payment_profiles.change_subscription_default_payment_profile

- **Route**: `POST /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def change_subscription_default_payment_profile(subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `payment_profile_id`
- **Params**: `subscription_id` — path · `payment_profile_id` — path
- **Returns (parsed)**: `PaymentProfileResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileResponse, ChangeSubscriptionDefaultPaymentProfileErrorBody]`
- **Error**: `ChangeSubscriptionDefaultPaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |
| `ChangeSubscriptionDefaultPaymentProfileErrorBody` | `maxio/errors/change_subscription_default_payment_profile_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.change_subscription_group_default_payment_profile

- **Route**: `POST /subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def change_subscription_group_default_payment_profile(uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`, `payment_profile_id`
- **Params**: `uid` — path · `payment_profile_id` — path
- **Returns (parsed)**: `PaymentProfileResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileResponse, ChangeSubscriptionGroupDefaultPaymentProfileErrorBody]`
- **Error**: `ChangeSubscriptionGroupDefaultPaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |
| `ChangeSubscriptionGroupDefaultPaymentProfileErrorBody` | `maxio/errors/change_subscription_group_default_payment_profile_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.create_payment_profile

- **Route**: `POST /payment_profiles.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def create_payment_profile(*, body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentProfileResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileResponse, CreatePaymentProfileErrorBody]`
- **Error**: `CreatePaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreatePaymentProfileRequest` | `maxio/models/create_payment_profile_request.py` |
| `CreatePaymentProfileRequestDict` | `maxio/models/create_payment_profile_request.py` |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |
| `CreatePaymentProfileErrorBody` | `maxio/errors/create_payment_profile_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.delete_subscription_group_payment_profile

- **Route**: `DELETE /subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def delete_subscription_group_payment_profile(uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `uid`, `payment_profile_id`
- **Params**: `uid` — path · `payment_profile_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.payment_profiles.delete_subscriptions_payment_profile

- **Route**: `DELETE /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def delete_subscriptions_payment_profile(subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `payment_profile_id`
- **Params**: `subscription_id` — path · `payment_profile_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.payment_profiles.delete_unused_payment_profile

- **Route**: `DELETE /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def delete_unused_payment_profile(payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_profile_id`
- **Params**: `payment_profile_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteUnusedPaymentProfileErrorBody]`
- **Error**: `DeleteUnusedPaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteUnusedPaymentProfileErrorBody` | `maxio/errors/delete_unused_payment_profile_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.list_payment_profiles

- **Route**: `GET /payment_profiles.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def list_payment_profiles(*, page: int | None = 1, per_page: int | None = 20, customer_id: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `customer_id` — query
- **Returns (parsed)**: `list[PaymentProfileResponse]`
- **Returns (raw)**: `ApiResult[list[PaymentProfileResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |

### client.payment_profiles.read_one_time_token

- **Route**: `GET /one_time_tokens/{chargify_token}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_one_time_token(chargify_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `chargify_token`
- **Params**: `chargify_token` — path
- **Returns (parsed)**: `GetOneTimeTokenRequest`
- **Returns (raw)**: `ApiResult[GetOneTimeTokenRequest, ReadOneTimeTokenErrorBody]`
- **Error**: `ReadOneTimeTokenErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOneTimeTokenRequest` | `maxio/models/get_one_time_token_request.py` |
| `ReadOneTimeTokenErrorBody` | `maxio/errors/read_one_time_token_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.read_payment_profile

- **Route**: `GET /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def read_payment_profile(payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_profile_id`
- **Params**: `payment_profile_id` — path
- **Returns (parsed)**: `PaymentProfileResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileResponse, ReadPaymentProfileErrorBody]`
- **Error**: `ReadPaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |
| `ReadPaymentProfileErrorBody` | `maxio/errors/read_payment_profile_error.py` |

### client.payment_profiles.send_request_update_payment_email

- **Route**: `POST /subscriptions/{subscription_id}/request_payment_profiles_update.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def send_request_update_payment_email(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SendRequestUpdatePaymentEmailErrorBody]`
- **Error**: `SendRequestUpdatePaymentEmailErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `SendRequestUpdatePaymentEmailErrorBody` | `maxio/errors/send_request_update_payment_email_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

### client.payment_profiles.update_payment_profile

- **Route**: `PUT /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def update_payment_profile(payment_profile_id: int, *, body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_profile_id`
- **Params**: `payment_profile_id` — path · `body` — JSON body
- **Returns (parsed)**: `PaymentProfileResponse`
- **Returns (raw)**: `ApiResult[PaymentProfileResponse, UpdatePaymentProfileErrorBody]`
- **Error**: `UpdatePaymentProfileErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorStringMapResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdatePaymentProfileRequest` | `maxio/models/update_payment_profile_request.py` |
| `UpdatePaymentProfileRequestDict` | `maxio/models/update_payment_profile_request.py` |
| `PaymentProfileResponse` | `maxio/models/payment_profile_response.py` |
| `UpdatePaymentProfileErrorBody` | `maxio/errors/update_payment_profile_error.py` |
| `ErrorStringMapResponse1` | `maxio/models/error_string_map_response1.py` |

### client.payment_profiles.verify_bank_account

- **Route**: `PUT /bank_accounts/{bank_account_id}/verification.json`
- **Auth**: `basic_auth`
- **Server**: `production`
- **Signature**: `def verify_bank_account(bank_account_id: int, *, body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bank_account_id`
- **Params**: `bank_account_id` — path · `body` — JSON body
- **Returns (parsed)**: `BankAccountResponse`
- **Returns (raw)**: `ApiResult[BankAccountResponse, VerifyBankAccountErrorBody]`
- **Error**: `VerifyBankAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListResponse1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `BankAccountVerificationRequest` | `maxio/models/bank_account_verification_request.py` |
| `BankAccountVerificationRequestDict` | `maxio/models/bank_account_verification_request.py` |
| `BankAccountResponse` | `maxio/models/bank_account_response.py` |
| `VerifyBankAccountErrorBody` | `maxio/errors/verify_bank_account_error.py` |
| `ErrorListResponse1` | `maxio/models/error_list_response1.py` |

