# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class owl_todo(models.Model):
#     _name = 'owl_todo.owl_todo'
#     _description = 'owl_todo.owl_todo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
