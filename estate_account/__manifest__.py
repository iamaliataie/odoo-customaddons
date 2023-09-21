# -*- coding: utf-8 -*-
{
    'name': "Estate Account",

    'summary': """
        Estate Account application to handle invoicing process for real estate application""",

    'description': """
        Estate Account application to handle invoicing process for real estate application
    """,

    'author': "Ali Ahmad Ataie",
    'website': "https://www.ataie.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'realestate', 'account'],
    'application': True,
    'sequence': -9999,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
