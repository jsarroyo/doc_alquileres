# -*- coding: utf-8 -*-
{
    'name': "DocAlquileres",

    'summary': """
        Documentos de alquiler""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bienes inmuebles',
    'version': '1.0',

    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['web'],
    
    # always loaded
    'data': [
        'data/actions.xml',
        'data/edificio_views.xml',
        'data/piso_views.xml',
        'data/local_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}