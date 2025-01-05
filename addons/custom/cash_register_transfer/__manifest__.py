# -*- coding: utf-8 -*-
{
    'name': "cash_register_transfer",
    'version': '0.1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',

    'summary': "Enable cash transfers between registers",

    'description': """
    This module allows transferring cash between registers using journal entries.
    """,

    'author': "Cyrus Nexus",
    'website': "https://www.CyrusNexus.com",


    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'base_accounting_kit'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cash_register_transfer_views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'application': False,
}

