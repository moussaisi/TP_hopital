# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital_App',
    'version': '1.0',
    'summary': 'Hospital Management',
    'sequence': 15,
    'description': """
Gestion Hopital 
====================
Ceci est une application de gestion qui a ete developpe en classe. 
Debut du projet : 10/06/2021
Fin du projet : /**/
    """,
    'category': 'Hospital',
    'depends': ['base'],
    'data': [
        'views/patient.xml',
        'views/medecin.xml',
        'views/grade.xml',
        'views/specialite.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False
}
