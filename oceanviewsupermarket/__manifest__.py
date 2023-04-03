
{
    'name': 'oceanviewsupermarket',
    'author': 'Akshaya',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/consumermanagement_views.xml',
        'views/accounting_views.xml',
        'views/goodsmanagement_views.xml',
        'views/workersmanagement.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False

}
