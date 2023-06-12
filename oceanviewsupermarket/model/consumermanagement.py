from odoo import models, fields, api


class ConsumerManagement(models.Model):
    _name = 'consumer.consumer'

    def _reminder_mail(self):
        reminder = self.env['consumer.consumer'].search([('start_date', '=', fields.Date.today())]).write({'active': False})
        print("one year completed",reminder)

    @api.model
    def _get_default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string='Name')
    consumer_no = fields.Integer(string='Consumer No')
    phone_number = fields.Char(string='Phone No')
    consumer_email = fields.Char(string='Email')
    image = fields.Image(string='Images')
    feedback = fields.Text(string='FeedBack')
    goods_ids = fields.Many2one('goods.goods', string='Goods Name')
    user_id = fields.Many2one('res.users', string='User', default=_get_default_user)
    goods_category = fields.Selection([
        ('fruits', 'Fruits'),
        ('meat&fish', 'Meat & Fish'),
        ('snacks', 'Snacks'),
        ('pasta', 'Pasta'),
        ('rice', 'Rice'),
        ('oils', 'Oils'),
        ('soups', 'Soups'),
        ('drinks', 'Drinks'),
        ('vegetables', 'Vegetables')],
        'Category'
    )
    start_date = fields.Date(string="Start Date")
    active = fields.Boolean('Active',default=True)

    # offer = fields.Selection([('10% off', '10% Off'),
    #                          ('20% off', '20% Off'),
    #                          ('50% off', '50% Off')], 'Offer',domain=[('goods_id','=','goods_ids')]


    list_of_goods = fields.Many2many(
        'goods.goods',
        string='List of Goods',
        domain="[('category','=',goods_category)]"
    )

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, '%s (%s)' % (record.consumer_no, record.name)))
        return res

    @api.onchange('first_name', 'last_name')
    def onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = '{} {}' .format(self.first_name, self.last_name)

    def action_goods_goods(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Consumer',
            'res_model': 'consumer.consumer',
            'view_mode': 'tree','form'
            'context': "{'create': False}"
        }




