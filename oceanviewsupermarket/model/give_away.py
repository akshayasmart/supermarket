from odoo import models,fields,api

class GiveAway(models.Model):
    _name = 'give.give'

    name = fields.Selection([('10% off','10% Off'),
    ('20% off','20% Off'),
    ('50% off','50% Off')],'Offer'
     )
    specialty_list= fields.Char(string='Specialty')
    image = fields.Image(string='Images')

    status_bar = fields.Selection([
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent'), ], 'Status Bar', default='temporary'
    )

    product_ids= fields.One2many('give.details','discount_id',string='Product')
    giveaway_status = fields.Selection([
        ('1 day offers', '1 Day Offers'),
        ('month_offers', 'Month Offers'), ],
          'giveaway_status'
    )
    deal = fields.Selection([('best deal','Best Deal'),
        ('new arrivals','New Arrivals')],
        'Deal'
      )


    @api.model
    def create(self, vals):
        print('>>>>>>>>', vals)
        vals['specialty_list'] = 'No Artificial colors'
        return super(GiveAway, self).create(vals)

    def write(self, vals):
        vals = self.giveaway_status(vals)
        res = super(GiveAway, self).write(vals)
        return res


class GiveAwayDetails(models.Model):
    _name = 'give.details'


    goods_id = fields.Many2one('goods.goods',string='Good')
    discount_id = fields.Many2one('give.give',string='Discounts')




