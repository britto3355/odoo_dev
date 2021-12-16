# -*- coding: utf-8 -*-
{
    'name': 'hospital managment',
    'version': '1.0',
    'summary': 'hospital managment software',
    'sequence': -100,
    'description': """hospital managment software""",
    'category': 'productivity',
    'website': 'https://www.odoohospitel.com',
    'license': 'LGPL-3',
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}