# outside
from time import sleep
import authentication
from threading import Thread
# inside
from the_invoices.invoice import invo
from the_invoices.webhook import event_webhoot

'''Thread, allows the_webhook and main functions to work simultaneously. at the same time.
one function works every 3 hours and the other every 3 minutes. But both run at the same time.'''


def main():
    # it was made with a work cycle, but it can be implemented with a datetime module. ex: difference_days function
    cicle = 8  # one day
    while cicle > 0:
        authentication.authe()
        invo()
        sleep(3)  # avoid queue issues (could have been done on lists)
        cicle -= 1
        sleep(10800)  # 3 hours in seconds


def the_webhook():
    while True:
        event_webhoot()
        sleep(180) #it does a check every 3 minutes




webhook = Thread(target=the_webhook)
my_main = Thread(target=main)
webhook.start()
my_main.start()

if __name__ == "__main__":
    main()
