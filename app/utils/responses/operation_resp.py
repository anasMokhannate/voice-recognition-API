from dataclasses import dataclass

@dataclass
class OperationResponse:
    intent: str 
    amount: int = None
    currency: str = None
    transaction_type: str = None
    confirmation_status: str = None
