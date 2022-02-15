from time import sleep
import authentication
from invoice import invo
from invoice_transfer import the_tranfers


def main():
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
