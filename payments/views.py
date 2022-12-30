# Create your views here.
from django.shortcuts import render
from gerencianet import Gerencianet

from credentials.credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


def home(request):
    body = {
        'calendario': {
            'expiracao': 3600
        },
        'devedor': {
            'cpf': '12345678909',
            'nome': 'Francisco da Silva'
        },
        'valor': {
            'original': '123.45'
        },
        'chave': '2f2924f3-78f3-4864-8e84-ee083c4f5bb0',
        'solicitacaoPagador': 'Cobrança dos serviços prestados.'
    }

    response = gn.pix_create_immediate_charge(body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
