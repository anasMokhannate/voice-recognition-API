from dataclasses import dataclass

@dataclass
class TransactionTypeResponse:
    intent: str = "select_transaction_type"
    transactionType : str 
