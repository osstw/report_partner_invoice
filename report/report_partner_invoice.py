# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class ReportPartnerInvoice(models.AbstractModel):
    _name = "report.report_partner_invoice.report_partner_invoice"

    @api.multi
    def render_html(self, data=None):
        docargs = {
            'doc_ids': self.ids,
            'doc_model': 'res.partner',
            'docs': self.env['res.partner'].browse(self.ids),
            'data': "this is my report",
        }
        return self.env['report'].render('report_partner_invoice.partner_invoice', values=docargs)
