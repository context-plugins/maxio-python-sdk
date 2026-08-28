from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..apple_pay_payment_profile import ApplePayPaymentProfile, ApplePayPaymentProfileDict
from ..bank_account_payment_profile import BankAccountPaymentProfile, BankAccountPaymentProfileDict
from ..credit_card_payment_profile import CreditCardPaymentProfile, CreditCardPaymentProfileDict
from ..paypal_payment_profile import PaypalPaymentProfile, PaypalPaymentProfileDict

PaymentProfile: TypeAlias = Annotated[
    ApplePayPaymentProfile | BankAccountPaymentProfile | CreditCardPaymentProfile | PaypalPaymentProfile,
    Field(discriminator="payment_type"),
]

PaymentProfileDict: TypeAlias = (
    ApplePayPaymentProfileDict | BankAccountPaymentProfileDict | CreditCardPaymentProfileDict | PaypalPaymentProfileDict
)
