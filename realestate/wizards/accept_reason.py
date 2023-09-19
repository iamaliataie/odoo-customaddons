from odoo import models, fields

class AcceptReasonWizard(models.TransientModel):
    _name = 'accept.reason.wizard'
    _description = 'Accept Reason Wizard'

    reason = fields.Text()
    property_id = fields.Many2one('realestate.property')
    date = fields.Date(default=fields.Date.context_today)

    