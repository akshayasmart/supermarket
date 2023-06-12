from odoo import fields, models



class PaymentWizard(models.TransientModel):
    _name =  'payment.payment'
    _description = 'Payment'

    consumer_no = fields.Char('Consumer No')
    amount = fields.Float(string='Amount')
    goods_ids = fields.Many2many('goods.goods', string='Goods')
    worker_ids = fields.Many2many('worker.worker', string='Workers')
    price = fields.Integer(string='Price')
    accounting_ids = fields.Many2many('accounting.accounting',string='Accounting')
    bank_name = fields.Char(string='Bank Name')
    # pay_ids = fields.One2many('pay.pay', 'payment_id' ,string='Payment')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')



    def print_report(self):
        data = {
            'accounting_ids': self.accounting_ids.ids,
            'bank_name': self.bank_name,
            'start_date': self.start_date,
            'end_date':self.end_date,

        }
        print('>>>>>>>>>>',data)
        return self.env.ref('oceanviewsupermarket.action_report_accounting').report_action(self, data=data)

    def print_worker(self):
        data = {
            'worker_ids': self.worker_ids.ids,
        }
        # data['form'].update({'worker_ids': self.worker_ids})
        return self.env.ref('oceanviewsupermarket.action_report_worker').report_action(self, data=data)


    def create_payments(self):
        goods_id = self.env.context.get('active_id')
        print('workiderrrrrrrrrrrrrr', goods_id)
        goods = self.env['goods.goods'].browse(goods_id)
        goods.write({
            'consumer_id': [
                (0, 0, {'consumer_ids': 7, 'price': 100}),
            ]
        })
        print ('goods_ids>>>>>>>>>>>>>>>>.', self.goods_ids.ids)
        payment = self.env['payment.details'].create({
            'consumer_no': self.consumer_no,
            'amount': self.amount,
            'goods_ids': [(6, 0,  self.goods_ids.ids)]
        })



# class Payment(models.Model):
#     _name = 'pay.pay'

    # goods_id = fields.Many2one('goods.goods', string='Goods')
    # consumer_id = fields.Many2one(
    #     'consumer.consumer',
    #     string="Consumer"
    # )

    # def create_payments(self):
    #     worker_id = self.env.context.get('active_id')
    #     print ('workiderrrrrrrrrrrrrr', worker_id)
    #     payment = self.env['goods.details'].browes(worker_id)
    #     vals= {
    #             'goods_ids': self.goods_ids,
    #             'consumer_ids': self.consumer_ids,
    #         }
    #     payment.write(vals)
