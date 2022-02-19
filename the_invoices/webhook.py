# outside
import starkbank
from datetime import timedelta, datetime
# inside
from transfer import trans


def event_webhoot():
    webhook = starkbank.webhook.get("6247777038237696")

    print(webhook)

    yesterday = datetime.now() - timedelta(1)
    yesterday.strftime('%d-%m-%Y')

    events = starkbank.event.query(after=yesterday, is_delivered=True)

    def the_file():
        with open("id_temp.txt", "a") as file:
            file.write("\n")
            file.write(event.log.invoice.id)

    for event in events:
        print(event.subscription)

        if event.subscription == "invoice":  # Some events may not be invoices
            if "paid" in event.log.invoice.status:  # "expired # "created"

                # Some events were generating duplicates in the Ids,
                # so this temporary file was created for control.
                # the same is deleted at the end of the session
                with open("id_temp.txt", "r") as file:
                    checando = file.read()

                if event.log.invoice.id not in checando:
                    the_file()
                    print("tranferencia criada:\n")
                    # Created the transfer, or the event not being an invoice.
                    # The event is excluded to not generate duplicates.

                    trans(event.log.invoice.amount)
                    # transfers = starkbank.transfer.create([
                    #     starkbank.Transfer(
                    #         amount=event.log.invoice.amount,
                    #         bank_code="20018183",  # TED
                    #         branch_code="0001",
                    #         account_number="6341320293482496",
                    #         tax_id="20.018.183/0001-80",
                    #         name="Stark Bank S.A.",
                    #         tags=["payment"]
                    #     )
                    # ])
                    # print(transfers)

                    event = starkbank.event.delete(event.id)
                    print(f"evento apagado {event}")

                else:
                    starkbank.event.delete(event.id)  # Delete repeated events

            elif "expired" in event.log.invoice.status:
                print(f"This invoice nº {event.log.invoice.id} has expired")

            elif "created" in event.log.invoice.status:

                print(f"This invoice nº {event.log.invoice.id} Created but not yet paid")

            else:

                print(f"This invoice nº {event.log.invoice.id} was already paid before")

        else:
            print("This event was not an invoice and will be deleted")

            event = starkbank.event.delete(event.id)

    with open("id_temp.txt", 'w') as file:
        pass
