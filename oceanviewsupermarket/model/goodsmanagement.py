from odoo import _,models, fields, api
from odoo.exceptions import UserError


class Goods(models.Model):
    _name = 'goods.goods'

    @api.model
    def _get_default_user(self):
        return self.env.context.get('user_id',self.env.user.id)

    @api.model
    def _get_default_user_name(self):
        return self.env.user.name

    name = fields.Char(string='Goods Name')
    goods_number = fields.Integer(string='Goods Number')
    expiry_date = fields.Date(string='Expiry Date')
    price = fields.Integer(string='Price')
    image = fields.Image(string='Images')
    start_date = fields.Datetime(string="Start Date")
    category = fields.Selection([
        ('fruits', 'Fruits'),
        ('meat&fish', 'Meat & Fish'),
        ('snacks', 'Snacks'),
        ('pasta', 'Pasta'),
        ('rice', 'Rice'),
        ('oils', 'Oils'),
        ('soups', 'Soups'),
        ('drinks', 'Drinks'),
        ('vegetables', 'Vegetables'),
        ('electronics','Electronics')], 'Category'
    )
    consumer_id = fields.One2many('goods.details', 'goods_ids', string='Consumers')
    total= fields.Float('total',compute="price_total")
    user_id = fields.Many2one('res.users',string='User',default=_get_default_user)
    user_name = fields.Char('Use Name', default=_get_default_user_name)
    consumer_no = fields.Integer(string='Consumer No')
    amount = fields.Float(string='Amount')
    goods_ids = fields.Many2one('goods.goods', string='Goods')



    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, '%s (%s)' % (record.goods_number, record.name)))
        return res


    @api.depends('consumer_id.price')
    def price_total(self):
         price_total =0
         for rec in self:
            for goods in rec.consumer_id:
                price_total += goods.price
            rec.total = price_total

    _sql_constraints = [
        ('goods_number_uniq', 'unique (goods_number)', 'The Goods Number must be unique !')
    ]

    # @api.constrains('price')
    # def _constraint_price(self):
    #     for record in self:
    #         if self.price < 1000:
    #             raise UserError(_(' All orders over $1000 it will be Free Delivery'))



class GoodsDetails(models.Model):
    _name = 'goods.details'

    goods_ids = fields.Many2one('goods.goods', string='Goods')
    consumer_ids = fields.Many2one('consumer.consumer', string='Consumer', domain="[('goods_ids', '=', goods_ids)]")
    category = fields.Selection(related="goods_ids.category",string='Goods Category')
    price = fields.Integer(string='Price')
    goods_number = fields.Integer(string='Goods Number')
