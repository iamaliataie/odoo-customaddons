from odoo import models, fields, api

class ResUser(models.Model):
    _inherit ='res.users'

    property_ids = fields.One2many('realestate.property', 'salesman', string='Properties', domain=[('state', 'in', ['new', 'offer_received'])])