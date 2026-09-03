from __future__ import annotations

from typing import TypeAlias

from ..payment_method_apple_pay import PaymentMethodApplePay, PaymentMethodApplePayDict
from ..payment_method_bank_account import PaymentMethodBankAccount, PaymentMethodBankAccountDict
from ..payment_method_credit_card import PaymentMethodCreditCard, PaymentMethodCreditCardDict
from ..payment_method_external import PaymentMethodExternal, PaymentMethodExternalDict
from ..payment_method_paypal import PaymentMethodPaypal, PaymentMethodPaypalDict

InvoiceEventPayment: TypeAlias = (
    PaymentMethodApplePay
    | PaymentMethodBankAccount
    | PaymentMethodCreditCard
    | PaymentMethodExternal
    | PaymentMethodPaypal
)
"""A nested data structure detailing the method of payment"""

InvoiceEventPaymentDict: TypeAlias = (
    PaymentMethodApplePayDict
    | PaymentMethodBankAccountDict
    | PaymentMethodCreditCardDict
    | PaymentMethodExternalDict
    | PaymentMethodPaypalDict
)
