# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    # Creating a plan in Gerencianet
    # body = {
    #     'name': "Meu Plano de Assinatura",
    #     'repeats': None,
    #     'interval': 1
    # }

    # response = gn.create_plan(params=None, body=body)
    # print(response)

    # id plan
    params = {
        'id': 9935
    }

    body = {
        'items': [{
            'name': "Product 1",
            'value': 1000,
            'amount': 2
        }],
        'payment': {
            'banking_billet': {
                'expire_at': '2023-01-31',
                'customer': {
                    'name': "Gorbadoc Oldbuck",
                    'email': "heitorlouzeiro2019@gmail.com",
                    'cpf': "94271564656",
                    'birth': "1977-01-15",
                    'phone_number': "5144916523"
                }
            }
        }
    }

    response = gn.one_step_subscription(params=params, body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
