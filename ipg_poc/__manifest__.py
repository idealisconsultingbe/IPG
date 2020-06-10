# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

{
    'name': 'IPG POC',
    'summary': 'Module offering all expectations from IPG POC',
    'version': '13.0.0.1',
    'description': """
Module offering all expectations from IPG POC
        """,
    'author': 'Idealis Consulting',
    'depends': [
        'base',
        'contacts',
        'sale_management',
        'stock',
        'project'
    ],
    'data': [
        'views/project_task_type_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
