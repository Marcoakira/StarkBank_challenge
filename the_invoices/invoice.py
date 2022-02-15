# outside
import starkbank
from random import randint
from datetime import datetime, timedelta
# inside
from data.cpf import generate_cpf
from data.name import name
from authentication import authe

authe()

invoices = []


def invo():
    one_invoice = starkbank.invoice.create([
        starkbank.Invoice(
            amount=randint(1, 99999),  # ex: R$ 235,71
            name=name(),
            tax_id=generate_cpf(),
            due=datetime.utcnow() + timedelta(hours=1),
            expiration=timedelta(hours=3).total_seconds(),
            fine=5,  # 5%
            interest=2.5,  # 2.5% per month
            tags=["immediate", "invoice"]
        )
    ])
    print(one_invoice)

    invoices.append(one_invoice)


for i in range(randint(8, 12)):
    invo()

for invoice in invoices:
    print(invoice)
