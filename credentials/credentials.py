import os

CREDENTIALS = {
    "client_id": os.environ.get('CLIENT_ID'),
    "client_secret": os.environ.get('CLIENT_SECRET'),
    'sandbox': True,
    # 'certificate': 'credentials/certificate/homologacao-429610-certficate.pem'
}
