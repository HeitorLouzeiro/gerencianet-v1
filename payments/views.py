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
        'shippings': [{
            'name': "Default Shipping Cost",
            'value': 100
        }]
    }

    response = gn.create_charge(body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
