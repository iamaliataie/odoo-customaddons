# -*- coding: utf-8 -*-
{
    'name': "owl_todo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'application': True,
    'sequence': -1000,
    'assets': {
        'web.assets_backend':[
            'owl_todo/static/src/components/*/*.js',
            'owl_todo/static/src/components/*/*.xml',
            'owl_todo/static/src/components/*/*.scss',
        ]
    }
}
