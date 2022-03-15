from typing import Tuple, List
from karrio.core.utils import Serializable
from karrio.core.models import (
    ShipmentCancelRequest,
    ConfirmationDetails,
    Message
)

from karrio.providers.asendia_us.error import parse_error_response
from karrio.providers.asendia_us.utils import Settings


def parse_shipment_cancel_response(response: dict, settings: Settings) -> Tuple[ConfirmationDetails, List[Message]]:
    errors = parse_error_response(response, settings)
    details = (
        ConfirmationDetails(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            operation="Shipment Cancel",
            success=True,
        )
        if not any(errors) else None
    )

    return details, errors


def shipment_cancel_request(payload: ShipmentCancelRequest, settings: Settings) -> Serializable:
    request = dict(
        packageID=payload.shipment_identifier,
        accountNumber=settings.account_number,
    )

    return Serializable(request)
