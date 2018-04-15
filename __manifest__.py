# -*- coding: utf-8 -*-
{
    'name': "doc_alquileres",

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
        'views/actions.xml',
        'views/edificio_views.xml',
        'views/piso_views.xml',
        'views/local_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}