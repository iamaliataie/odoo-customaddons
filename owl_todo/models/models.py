# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OwlTodo(models.Model):
    _name = 'owl.todo.list'
    _description = 'Owl Todo List Model'

    name = fields.Char(string='Task Name')
    color = fields.Char()
    completed = fields.Boolean()

