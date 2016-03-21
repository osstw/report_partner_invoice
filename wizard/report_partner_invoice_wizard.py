# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class ReportPartnerInvoiceWizard(models.Model):
    _name = "report_partner_invoice.wizard"

    partner_id = fields.Many2one("res.partner")

    date_from = fields.Date()
    date_to = fields.Date()

    @api.multi
    def action_OK(self):
        self.ensure_one()
        data = dict()
        if all((self.date_from, self.date_to)):
            data["date_from"] = self.date_from
            data["date_to"] = self.date_to
        data["partner_id"] = self.partner_id.id

        return self.env['report'].get_action(self, 'report_partner_invoice.report_partner_invoice', data=data)


