from odoo import models, fields, api


class ReportWorker(models.AbstractModel):
    _name = 'report.oceanviewsupermarket.report_worker'
    _description = 'Report Worker'

    @api.model
    def _get_report_values(self, docids, data=None):
        worker_ids = data['worker_ids']
        docs = self.env['worker.worker'].browse(worker_ids)
        return {
            'doc_ids': docids,
            'doc_model': 'worker.worker',
            'docs': docs,
        }
