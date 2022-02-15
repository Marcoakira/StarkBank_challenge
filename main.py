from time import sleep
import authentication
from invoice import invo
from invoice_transfer import the_tranfers

cicle = 8 #one day
while cicle > 0:

    authentication.authe()
    invo()
    sleep(3)  # evitar problemas de fila ( poderia ter sido feito em listas)
    the_tranfers()
    cicle = - 1
    sleep(10800) # 3 hours in seconds


