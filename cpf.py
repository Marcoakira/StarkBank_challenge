# outside
import requests

''' pt-Br
The API chosen to generate the valid cpf had little documentation, and it does a validation with Token
in the header. So, using the solution proposed by the REQUEST documentation
https://docs.python-requests.org/pt_BR/latest/user/authentication.html. in new forms of authentication.
'''


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def generate_cpf():
    response = requests.get('https://gerador.app/api/cpf/generate',
                            auth=BearerAuth('CRHIT0EhJrBb72n6nWhB7goOOs3OUtOMouzcrEN0'))
    # replace BearerAuth with your token key
    response = response.json()
    new_cpf = response['number']

    return new_cpf
