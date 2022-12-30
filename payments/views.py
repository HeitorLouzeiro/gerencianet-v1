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
    transaction_id = response['data']['charge_id']

    params = {
        'id': transaction_id
    }
    body = {
        'title': 'Balancete Demonstrativo',
        'body': [
            {
                'header': 'Demonstrativo de Consumo',
                'tables': [
                    {
                        'rows': [
                            [
                                {
                                    'align': 'left',
                                    'color': '#000000',
                                    'style': 'bold',
                                    'text': 'Exemplo de despesa',
                                    'colspan': 2
                                },
                                {
                                    'align': 'left',
                                    'color': '#000000',
                                    'style': 'bold',
                                    'text': 'Total lançado',
                                    'colspan': 2
                                }
                            ],
                            [
                                {
                                    'align': 'left',
                                    'color': '#000000',
                                    'style': 'normal',
                                    'text': 'Instalação',
                                    'colspan': 2
                                },
                                {
                                    'align': 'left',
                                    'color': '#000000',
                                    'style': 'normal',
                                    'text': 'R$ 100,00',
                                    'colspan': 2
                                }
                            ]
                        ]
                    }
                ]
            },
            {
                'header': 'Balancete Geral',
                'tables': [
                    {
                        'rows': [
                            [
                                {
                                    'align': 'left',
                                    'color': '#000000',
                                    'style': 'normal',
                                    'text': 'Confira na documentação da Gerencianet todas as configurações possíveis.',
                                    'colspan': 4
                                }
                            ]
                        ]
                    }
                ]
            }
        ]
    }

    response = gn.create_charge_balance_sheet(params=params, body=body)
    print(response)
    return render(request, 'payments/pages/home.html')
