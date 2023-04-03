from odoo import models, fields


class Accounting(models.Model):
    _name = 'accounting.accounting'

    name = fields.Char(string='Account Name')
    account_number = fields.Char(string='Account Number')
    ifsc_code = fields.Char(string='IFSC')
    phone_number = fields.Char(string='Phone No')
    opening_balance = fields.Integer(string='Opening Balance')
    profits = fields.Integer(string='Profits')
    image = fields.Image(string='Images')
    start_date = fields.Datetime(string="Start Date")
    bank_name = fields.Char(string='Bank Name')
