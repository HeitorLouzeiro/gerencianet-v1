# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    body = {
        'items': [{
            'name': "Product 1",
            'value': 1000,
            'amount': 2
        }],
        'payment': {
            'credit_card': {
                'installments': 5,
                'payment_token': "abe5cec2500bbd2ced45bc728ca1ce9015278bc5",
                'billing_address': {
                    'street': "Av. JK",
                    'number': 909,
                    'neighborhood': "Bauxita",
                    'zipcode': "35400000",
                    'city': "Ouro Preto",
                    'state': "MG"
                },
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
    response = gn.create_charge_onestep(params=None, body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
