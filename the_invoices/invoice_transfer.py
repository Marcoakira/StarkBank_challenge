'''
DESATIVADO, NÃO FAZ MAIS PARTE DA SOLUÇÃO, MANTIVE APENAS PARA COMPARAÇÃO.
# outside
import starkbank
from datetime import datetime
# inside
from transfer import trans

invoices = starkbank.invoice.query()


def diferenca_dias(d1, d2):
    print((d2 - d1).seconds)
    return ((d2 - d1).seconds)


now = datetime.now()


def the_tranfers():
    for i in invoices:

        the_time = diferenca_dias(now, i.created)
        if the_time < 5400:  # this is the time range of one and a half hours. either forward or past
            # (takes the time difference into account)
            trans(i.amount)

'''
