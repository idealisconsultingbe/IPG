# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.project_ids:
                order.project_id = order.project_ids[0]
                for task in order.project_id.task_ids:
                    task.state = self.env['project.task.type'].search([('tests_commandes', '=', True)]).id
        return res
