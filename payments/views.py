# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    body = {
        'items': [{
            'name': "Couse 1",
            'value': 1000,
            'amount': 2
        }],
        'shippings': [{
            'name': "Default Shipping Cost",
            'value': 100
        }],
        'payment': {
            'banking_billet': {
                'expire_at': '2023-01-01',
                'customer': {
                    'name': "Gorbadoc Oldbuck",
                    'email': "heitorlouzeiro2019@gmail.com",
                    'cpf': "14014603059",
                    'birth': "1977-01-15",
                    'phone_number': "62986070247"

                }
            }
        }
    }
    response = gn.create_charge_onestep(params=None, body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
