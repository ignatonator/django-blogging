from storages.backends.azure_storage import AzureStorage
class AzureMediaStorage(AzureStorage):
    account_name = 'mediadjango'
    account_key = 'LNfNwIStdRiekpoCy7aIzDCDHabbFy94g/DRuVoLkEOECj7BeoJ98uwYM3Ml83CSqxoY0TAdV4XLGW5KI+FT7w=='
    azure_container = 'media'
    expiration_secs = None