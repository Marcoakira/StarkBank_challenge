# outside
from time import sleep
import authentication
# inside
from the_invoices.invoice import invo
from the_invoices.invoice_transfer import the_tranfers


def main():
    # it was made with a work cycle, but it can be implemented with a datetime module. ex: difference_days function
    cicle = 8  # one day
    while cicle > 0:
        authentication.authe()
        invo()
        sleep(3)  # avoid queue issues (could have been done on lists)
        the_tranfers()
        cicle = - 1
        sleep(10800)  # 3 hours in seconds


if __name__ == "__main__":
    main()

"""

TODO next implementation: the webhook will replace the inoives_transfer. making a more complete integration
with the webhook.site

from webhook import webhooksite

webhooksite()

"""
