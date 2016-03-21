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
        amount_payable = int(round(sum(inv.amount_total for inv in invoices), 0))
        residual_total = int(round(sum(inv1.residual for inv1 in invoices), 0))
        balance_payable = int(round((amount_payable - residual_total), 0))
        docargs = {
            "partner": partner,
            "invoices": invoices,
            "amount_total": amount_payable,
            "residual_total": residual_total,
            "balance_payable": balance_payable,
        }

        return self.env['report'].render('report_partner_invoice.report_partner_invoice_template', values=docargs)
