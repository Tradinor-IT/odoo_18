# -*- coding: utf-8 -*-
{
    'name'          : 'College Management',
    'version'       : '18.0.1.0,0',
    'summary'       : 'college erp',
    'sequence'      : 10,

    # any module necessary for this one to work correctly
    'depends'       : ['base'],
    'license'       : 'OPL-1',
    'maintainer'    : '',
    'company'       : '',
    'description'   : 'College details',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_record_view.xml',
        #'views/templates.xml',
    ],
    'author': "Cyrus-Nexus",
    'installation'  : True,
    'auto_install'  : False,
    'application'   : True
}

