from odoo import _,models, fields,api


class Accounting(models.Model):
    _name = 'accounting.accounting'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Account Name')
    account_number = fields.Char(string='Account Number')
    ifsc_code = fields.Char(string='IFSC')
    phone_number = fields.Char(string='Phone No')
    opening_balance = fields.Integer(string='Opening Balance')
    profits = fields.Integer(string='Profits')
    image = fields.Image(string='Images')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    bank_name = fields.Char(string='Bank Name')

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if 'account_number' not in default:
            default['account_number'] = _("%s (duplicate)") % self.account_number
        return super(Accounting, self).copy(default=default)

    @api.model
    def create(self, vals):
          print('>>>>>>>>',vals)
          vals['bank_name'] = 'SBI'
          return super(Accounting, self).create(vals)


    # def add(self):
    #     self.create({"name": "Bowmika","account_list":[(0,0, {"name":"Bowmika 1","account_number":89890664}),
    #                                                    (0, 0, {"name": "Sneha 2","account_number":3564673784564})]})
    # 


