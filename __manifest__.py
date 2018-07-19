# -*- coding: utf-8 -*-
{
    'name': "rfid",

    'summary': """
        this modules read rfid tag from API""",

    'description': """
        Check TAG using intellifi RFID for supply chain mechanism at B4T. 
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
        'static/src/xml/supporthtmlset.xml',
        #'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'qweb': ['static/src/xml/qweb.xml'],
}