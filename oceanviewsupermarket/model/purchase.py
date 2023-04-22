from odoo import models, fields,api

class Purchase(models.Model):
     _inherit = 'purchase.order'

     # @api.depends('order_line.price_total','product_price')
     # def _amount_all(self):
     #     for order in self:
     #         amount_untaxed = amount_tax = 0.0
     #         for line in order.order_line:
     #             line._compute_amount()
     #             amount_untaxed += line.price_subtotal
     #             amount_tax += line.price_tax
     #         currency = order.currency_id or order.partner_id.property_purchase_currency_id or self.env.company.currency_id
     #         order.update({
     #             'amount_untaxed': currency.round(amount_untaxed),
     #             'amount_tax': currency.round(amount_tax),
     #             'amount_total': amount_untaxed + amount_tax,
     #             'total_amount' : amount_untaxed + amount_tax + order.total_amount
     #         })

     @api.model
     def _get_mrp_productions(self):
         print('>>>>>>>>>>>>>>>>>.')
         res = super(Purchase,self)._get_mrp_productions()
         return res

     @api.depends('order_line.price_total','product_price')
     def _purchase_amount_all(self):
         for order in self:
             amount_untaxed = amount_tax = 0.0
             for line in order.order_line:
                 amount_untaxed += line.price_subtotal
                 amount_tax += line.price_tax
             order.update({
                 'total_amount' : amount_untaxed + amount_tax + order.total_amount
             })


     category = fields.Selection([
         ('fruits', 'Fruits'),
         ('meat&fish', 'Meat & Fish'),
         ('pasta', 'Pasta'),
         ('rice', 'Rice'),
         ('oils', 'Oils'),
         ('soups', 'Soups'),
         ('drinks', 'Drinks'),
         ('vegetables', 'Vegetables')], 'Category'
     )
     product_price = fields.Integer(string="Product Price")
     total_amount = fields.Monetary(compute='_purchase_amount_all' ,string='Total Amount')


class PurchaseLine(models.Model):
    _inherit = 'purchase.order.line'

    product_code = fields.Integer("Product Code")
