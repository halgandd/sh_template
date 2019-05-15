# -*- coding: utf-8 -*-
# Copyright (C) 2019 - Teclib'ERP (<https://www.teclib-erp.com>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'test',
    'version': '1.0',
    'author': 'Teclib ERP',
    'website': 'https://www.teclib-erp.com',
    'summary': "Teclib'ERP",
    'sequence': 0,
    'certificate': '',
    'license': 'LGPL-3',
    'depends': [
        'web',
        'base',
    ],
    'category': 'Generic Modules/Teclib ERP',
    'complexity': 'easy',
    'description': '''
description
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/test_test_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}