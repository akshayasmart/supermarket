# from odoo import models, fields, api
#
#
# class ReportAccounting(models.AbstractModel):
#     _name = 'report.oceanviewsupermarket.report_account'
#     _description = 'Report Account'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         print('>>>>>',data)
#         accounting_ids = data['accounting_ids']
#         docs = self.env['accounting.accounting'].search(['|',('id', 'in', accounting_ids),('bank_name','ilike',data['bank_name']),
#                             ('start_date','>=',data['start_date']),('end_date','<=',data['end_date'])])
#         print('>>>>>>>>>>>>>>>',docs)
#         return {
#             'doc_ids': docids,
#             'doc_model': 'accounting.accounting',
#             'docs': docs,
#         }
#
#
