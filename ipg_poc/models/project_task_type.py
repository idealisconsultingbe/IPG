# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    tests_commandes = fields.Boolean(string='Tests Commandés')


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def create(self, vals):
        context = dict(self.env.context)
        res = super(ProjectTask, self.with_context(context)).create(vals)
        if not vals.get('parent_id'):
            tc = self.env['project.task.type'].search([('tests_commandes', '=', True)], limit=1).id
            res.stage_id = tc
        return res
