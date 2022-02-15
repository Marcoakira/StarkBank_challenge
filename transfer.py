# outside
import starkbank
# inside
from authentication import authe

authe()


def trans(money):
    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount=money,
            bank_code="20018183",  # TED
            branch_code="0001",
            account_number="6341320293482496",
            tax_id="20.018.183/0001-80",
            name="Stark Bank S.A.",
            tags=["payment"]
        )
    ])
    print(transfers)
