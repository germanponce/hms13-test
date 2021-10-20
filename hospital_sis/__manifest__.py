# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

{
    'name': 'Sistema de Información Hospitalario SIS-1',
    'version': '1.1',
    'author': 'Marlon Falcon Hernandez',
    'maintainer': "Leonardo J. Caballero G.",
    'category': 'Accounting & Finance',
    'summary': 'Modulo de gestión de hospital 2016 - 2019',
    'sequence': 30,
    'website': 'https://www.marlonfalcon.cl',
    'description': """
It is an example module
=======================
With this module we will make our first application in Odoo.

 * One

 * Two

Note: You need the 'Sales' application.
    """,
    'license': 'AGPL-3',
    'depends': ['sale', 'base_setup', 'product', 'analytic'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/hospital_view.xml',
        'views/specialty_view.xml',
        'views/laboratory_view.xml',
        'views/consultation_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'active': False,
    'auto_install': False,
    'demo': [
        'demo/demo.xml',
    ],
}
