
{
    'name': 'oceanviewsupermarket',
    'author': 'Akshaya',
    'version': '0.1',
    'depends': ['base','purchase','mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/goods_data.xml',
        'report/report_worker.xml',
        'report/report_accounting.xml',
        'wizard/payment_view.xml',
        'views/goodsmanagement_views.xml',
        'views/consumermanagement_views.xml',
        'views/give_away_views.xml',
        'views/accounting_views.xml',
        'views/workersmanagement.xml',
        'views/payment.xml',
        'views/purchase.xml',
        'views/ocean_report.xml',
        'views/goods_report.xml',
        'data/cron_data.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
