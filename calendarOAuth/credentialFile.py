
def getClientConfig():
    
    cliend_id = '997569035244-6lmm969hvc0tcih1i16e8koektg19g7u.apps.googleusercontent.com'
    project_id = 'convinn'
    auth_uri = 'https://accounts.google.com/o/oauth2/auth'
    token_uri = 'https://oauth2.googleapis.com/token'
    auth_provider_x509_cert_url = 'https://www.googleapis.com/oauth2/v1/certs'
    client_secret = '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'
    redirect_uris = ["http://127.0.0.1:8000/about"]

    return {"web":{"client_id":cliend_id,"project_id":project_id,"auth_uri":auth_uri,"token_uri":token_uri,"auth_provider_x509_cert_url":auth_provider_x509_cert_url,"client_secret":client_secret,"redirect_uris":redirect_uris}}