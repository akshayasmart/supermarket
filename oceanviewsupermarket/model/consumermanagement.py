from odoo import models, fields


class Consumermanagement(models.Model):
    _name = 'consumer.consumer'

    name = fields.Char(string='Name')
    consumer_id = fields.Integer(string='Consumer Id')
    phone_number = fields.Char(string='Phone No')
    consumer_email = fields.Char(string='Email')
    image = fields.Image(string='Images')
    feedback = fields.Text(string='FeedBack')
    goods_name = fields.Many2one('goods.goods', string='Goods Name')
    list_of_goods = fields.Many2many('goods.goods',string='List of Goods',domain=[('category','=','goods_name')])

