# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    params = {
        'id': 1785912
    }
    body = {
        'payment': {
            'banking_billet': {
                'expire_at': '2022-12-31',
                'customer': {
                    'name': "Gorbadoc Oldbuck",
                    'email': "oldbuck@gerencianet.com.br",
                    'cpf': "94271564656",
                    'birth': "1977-01-15",
                    'phone_number': "5144916523"
                }
            }
        }
    }

    response = gn.pay_charge(params=params, body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
