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
        'project',
        'contacts',
        'sale_management',
        'sale_timesheet',
        'stock',
    ],
    'data': [
        'views/project_task_type_view.xml',
        'views/stock_move_line_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
