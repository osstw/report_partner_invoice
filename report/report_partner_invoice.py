# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class ReportPartnerInvoice(models.AbstractModel):
    _name = "report.report_partner_invoice.report_partner_invoice"

    @api.multi
    def render_html(self, data=None):
        partner_id = data.get("partner_id", None)
        if not partner_id:
            return

        partner = self.env["res.partner"].browse(partner_id)
        invoices = self.env["account.invoice"].search([("partner_id", "=", partner_id),
                                                       ("state", "=", "open")])
        amount_total = sum(inv.amount_total for inv in invoices)
        docargs = {
            "partner": partner,
            "invoices": invoices,
            "amount_total": amount_total
        }

        return self.env['report'].render('report_partner_invoice.report_partner_invoice_template', values=docargs)
