# -*- coding: utf-8 -*-
{
    'name': "rfid",

    'summary': """
        this modules read rfid tag from API""",

    'description': """
        API RFID from intellifi make http request and get the HEX Code. 
    """,

    'author': "B4T",
    'website': "http://www.b4t.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/mymenu.xml',
        'views/mainview.xml',
        'views/tag.xml',
        'dummies/listtag.xml',
        'views/polybox_list.xml',
        #'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}