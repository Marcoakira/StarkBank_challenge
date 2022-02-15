import starkbank
from datetime import datetime
from transfer import trans

invoices = starkbank.invoice.query()


def diferenca_dias(d1, d2):
    print((d2 - d1).seconds)
    return ((d2 - d1).seconds)


now = datetime.now()
def the_tranfers():
    for i in invoices:

        the_time = diferenca_dias(now, i.created)
        if the_time < 5400:  # esse é o range de tempo de uma hora e meia. seja para frente ou que ja passou
            # ( leva em consideração a diferença de fuso)
            trans(i.amount)
