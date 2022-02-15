import starkbank


# Use your private key, they are always in pairs, Public/private.
# This is just an example of private key content. You must use your own key.
# There are many ways to get your keys.
# Don't forget to previously send your public key (pair of this key) to the sandbox.
# More information https://starkbank.com/faq/how-to-create-ecdsa-keys.

def authe():
    private_key_content = """
    -----BEGIN EC PARAMETERS-----
    BgUrgQQACg==
    -----END EC PARAMETERS-----
    -----BEGIN EC PRIVATE KEY-----
###########  INSIRA AQUI SUA KEY  #############
    -----END EC PRIVATE KEY-----
    
    """
    # Important: Attention if they are by project, or Organization. ex: starkbank.Project or starkbank.Organization
    # In the Id field, put the Id of the project created in the sandbox.
    project = starkbank.Project(
        environment="sandbox",
        id="5397225257566208",
        private_key=private_key_content,

    )

    # here we authenticate
    starkbank.user = project  # or organization

    # Language options are "en-US" for english and "pt-BR" for brazilian portuguese. English is default.
    starkbank.language = "pt-BR"
    balance = starkbank.balance.get(user=project)  # or organization, # valor do caixa

    return project
