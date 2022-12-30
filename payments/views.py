# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    body = {
        'items': [{
            'name': 'Carnet Item 1',
            'value': 1000,
            'amount': 2
        }],
        'customer': {
            'name': 'Gorbadoc Oldbuck',
            'email': 'oldbuck@gerencianet.com.br',
            'cpf': '94271564656',
            'birth': '1977-01-15',
            'phone_number': '5144916523'
        },
        'repeats': 3,
        'expire_at': '2023-01-01'
    }
    response = gn.create_carnet(body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
