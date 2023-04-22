from odoo import models,fields


class Payment(models.Model):
    _name = 'payment.details'

    receipt_no = fields.Integer(string="Receipt No")
    consumer_no = fields.Char(string='Consumer No')
    goods_number = fields.Integer(string='Goods Number')
    date = fields.Date(string='Date')
    amount = fields.Float(string='Amount')

    payment_method = fields.Selection([
        ('phone_pe','Phone pe'),
        ('upi','UPI'),
        ('account_transfer','Account Transfer')],'Payment Method'
    )
    goods_ids = fields.Many2many('goods.goods', string='Goods')
