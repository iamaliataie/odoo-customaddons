from odoo import models, fields, Command, api

class Property(models.Model):
    _inherit = 'realestate.property'

    invoice_id = fields.Many2one('account.move')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    invoice_amount = fields.Monetary(compute='_compute_invoice_amount')


    @api.depends('invoice_id')
    def _compute_invoice_amount(self):
        for rec in self:
            rec.invoice_amount = 0
            if rec.invoice_id:
                rec.invoice_amount = rec.invoice_id.amount_total


    def action_sold(self):
        invoice = self.env['account.move'].create({
            'partner_id': self.buyer.id,
            'move_type': 'out_invoice',
            'property_id': self.id,
            'invoice_line_ids': [
                Command.create({
                    'name': f'6% of {self.name}({self.selling_price})',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                    'tax_ids': [(5,0,0)],
                }),
                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1,
                    'price_unit': 100,
                    'tax_ids': [(5,0,0)],
                })
            ]
        })

        self.invoice_id = invoice.id
        return super(Property, self).action_sold()

    def open_invoice(self):
        for rec in self:
            return {
                'name': 'Invoice',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': rec.invoice_id.id,
            }


class AccountMove(models.Model):
    _inherit = 'account.move'

    property_id = fields.Many2one('realestate.property')

    def open_property(self):
        for rec in self:
            return {
                'name': 'Property',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'realestate.property',
                'res_id': rec.property_id.id,
            }