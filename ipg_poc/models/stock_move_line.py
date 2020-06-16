# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    x_studio_test_ids = fields.Many2many('project.task', 'x_project_task_stock_move_line_rel_1',
                                         'stock_move_line_id', 'project_task_id', string='Tasks')
    project_id = fields.Many2one('project.project', related='picking_id.sale_id.project_id', store=True, readonly=True)
    #
    # @api.depends('picking_id.sale_id')
    # def _compute_project_ids(self):
    #     for line in self:
    #         if line.picking_id.sale_id:
    #             line.project_ids = line.picking_id.sale_id.project_ids


