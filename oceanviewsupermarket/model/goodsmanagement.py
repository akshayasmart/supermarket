from odoo import models, fields


class Goods(models.Model):
    _name = 'goods.goods'

    name = fields.Char(string='Goods Name')
    goods_id = fields.Integer(string='Goods ID')
    expiry_date = fields.Date(string='Expiry Date')
    price = fields.Integer(string='Price')
    image = fields.Image(string='Images')
    start_date = fields.Datetime(string="Start Date")
    category = fields.Selection([('fruits', 'Fruits'),
                                 ('meat&fish', 'Meat & Fish'),
                                 ('snacks', 'Snacks'),
                                 ('pasta', 'Pasta'),
                                 ('rice', 'Rice'),
                                 ('oils', 'Oils'),
                                 ('soups', 'Soups'),
                                ('drinks', 'Drinks'),
                                 ('vegetables', 'Vegetables')
                                 ], 'Category')
    consumer_name = fields.One2many('consumer.consumer','goods_name',string='Consumer Name')

