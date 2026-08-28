<!-- Generated file — do not edit; regenerated with the SDK. -->

# EventsBasedBillingSegments — operations

Accessor: `client.events_based_billing_segments` · Source: `maxio/apis/events_based_billing_segments.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.events_based_billing_segments.bulk_create_segments

- **Route**: `POST /components/{component_id}/price_points/{price_point_id}/segments/bulk.json`
- **Server**: `production`
- **Signature**: `def bulk_create_segments(component_id: str, price_point_id: str, *, body: BulkCreateSegments | BulkCreateSegmentsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`
- **Params**: `component_id` — path · `price_point_id` — path · `body` — JSON body
- **Returns (parsed)**: `ListSegmentsResponse`
- **Returns (raw)**: `ApiResult[ListSegmentsResponse, BulkCreateSegmentsErrorBody]`
- **Error**: `BulkCreateSegmentsErrorBody` — **Case A (typed)**
- **Error arms**: `EventBasedBillingSegment1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `BulkCreateSegments` | `maxio/models/bulk_create_segments.py` |
| `BulkCreateSegmentsDict` | `maxio/models/bulk_create_segments.py` |
| `ListSegmentsResponse` | `maxio/models/list_segments_response.py` |
| `BulkCreateSegmentsErrorBody` | `maxio/errors/bulk_create_segments_error.py` |
| `EventBasedBillingSegment1` | `maxio/models/event_based_billing_segment1.py` |

### client.events_based_billing_segments.bulk_update_segments

- **Route**: `PUT /components/{component_id}/price_points/{price_point_id}/segments/bulk.json`
- **Server**: `production`
- **Signature**: `def bulk_update_segments(component_id: str, price_point_id: str, *, body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`
- **Params**: `component_id` — path · `price_point_id` — path · `body` — JSON body
- **Returns (parsed)**: `ListSegmentsResponse`
- **Returns (raw)**: `ApiResult[ListSegmentsResponse, BulkUpdateSegmentsErrorBody]`
- **Error**: `BulkUpdateSegmentsErrorBody` — **Case A (typed)**
- **Error arms**: `EventBasedBillingSegment1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `BulkUpdateSegments` | `maxio/models/bulk_update_segments.py` |
| `BulkUpdateSegmentsDict` | `maxio/models/bulk_update_segments.py` |
| `ListSegmentsResponse` | `maxio/models/list_segments_response.py` |
| `BulkUpdateSegmentsErrorBody` | `maxio/errors/bulk_update_segments_error.py` |
| `EventBasedBillingSegment1` | `maxio/models/event_based_billing_segment1.py` |

### client.events_based_billing_segments.create_segment

- **Route**: `POST /components/{component_id}/price_points/{price_point_id}/segments.json`
- **Server**: `production`
- **Signature**: `def create_segment(component_id: str, price_point_id: str, *, body: CreateSegmentRequest | CreateSegmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`
- **Params**: `component_id` — path · `price_point_id` — path · `body` — JSON body
- **Returns (parsed)**: `SegmentResponse`
- **Returns (raw)**: `ApiResult[SegmentResponse, CreateSegmentErrorBody]`
- **Error**: `CreateSegmentErrorBody` — **Case A (typed)**
- **Error arms**: `EventBasedBillingSegmentErrors1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateSegmentRequest` | `maxio/models/create_segment_request.py` |
| `CreateSegmentRequestDict` | `maxio/models/create_segment_request.py` |
| `SegmentResponse` | `maxio/models/segment_response.py` |
| `CreateSegmentErrorBody` | `maxio/errors/create_segment_error.py` |
| `EventBasedBillingSegmentErrors1` | `maxio/models/event_based_billing_segment_errors1.py` |

### client.events_based_billing_segments.delete_segment

- **Route**: `DELETE /components/{component_id}/price_points/{price_point_id}/segments/{id}.json`
- **Server**: `production`
- **Signature**: `def delete_segment(component_id: str, price_point_id: str, id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`, `id`
- **Params**: `component_id` — path · `price_point_id` — path · `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteSegmentErrorBody]`
- **Error**: `DeleteSegmentErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, 422, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteSegmentErrorBody` | `maxio/errors/delete_segment_error.py` |

### client.events_based_billing_segments.list_segments_for_price_point

- **Route**: `GET /components/{component_id}/price_points/{price_point_id}/segments.json`
- **Server**: `production`
- **Signature**: `def list_segments_for_price_point(component_id: str, price_point_id: str, *, page: int | None = 1, per_page: int | None = 30, filter: ListSegmentsFilter | ListSegmentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`
- **Params**: `component_id` — path · `price_point_id` — path · `page` — query · `per_page` — query · `filter` — query
- **Returns (parsed)**: `ListSegmentsResponse`
- **Returns (raw)**: `ApiResult[ListSegmentsResponse, ListSegmentsForPricePointErrorBody]`
- **Error**: `ListSegmentsForPricePointErrorBody` — **Case A (typed)**
- **Error arms**: `EventBasedBillingListSegmentsErrors1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `ListSegmentsFilter` | `maxio/models/list_segments_filter.py` |
| `ListSegmentsFilterDict` | `maxio/models/list_segments_filter.py` |
| `ListSegmentsResponse` | `maxio/models/list_segments_response.py` |
| `ListSegmentsForPricePointErrorBody` | `maxio/errors/list_segments_for_price_point_error.py` |
| `EventBasedBillingListSegmentsErrors1` | `maxio/models/event_based_billing_list_segments_errors1.py` |

### client.events_based_billing_segments.update_segment

- **Route**: `PUT /components/{component_id}/price_points/{price_point_id}/segments/{id}.json`
- **Server**: `production`
- **Signature**: `def update_segment(component_id: str, price_point_id: str, id: float, *, body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `component_id`, `price_point_id`, `id`
- **Params**: `component_id` — path · `price_point_id` — path · `id` — path · `body` — JSON body
- **Returns (parsed)**: `SegmentResponse`
- **Returns (raw)**: `ApiResult[SegmentResponse, UpdateSegmentErrorBody]`
- **Error**: `UpdateSegmentErrorBody` — **Case A (typed)**
- **Error arms**: `EventBasedBillingSegmentErrors1` [422] · `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSegmentRequest` | `maxio/models/update_segment_request.py` |
| `UpdateSegmentRequestDict` | `maxio/models/update_segment_request.py` |
| `SegmentResponse` | `maxio/models/segment_response.py` |
| `UpdateSegmentErrorBody` | `maxio/errors/update_segment_error.py` |
| `EventBasedBillingSegmentErrors1` | `maxio/models/event_based_billing_segment_errors1.py` |

