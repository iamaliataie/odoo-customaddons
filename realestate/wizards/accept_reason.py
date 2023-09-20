from odoo import models, fields

class AcceptReasonWizard(models.TransientModel):
    _name = 'accept.reason.wizard'
    _description = 'Accept Reason Wizard'

    reason = fields.Text()
    property_id = fields.Many2one('realestate.property')
    offer_id = fields.Many2one('realestate.property.offer')
    date = fields.Date(default=fields.Date.context_today)

    def action_accept(self):
        for rec in self:
            rec.property_id.write(({
                'selling_price': rec.offer_id.price,
                'buyer': rec.offer_id.partner_id.id,
                'state': 'offer_accepted',
            }))
            rec.offer_id.state = 'accepted'