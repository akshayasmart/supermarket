from odoo import models,fields

class Workersmanagement(models.Model):
    _name = 'worker.worker'

    name = fields.Char(string='Employee Name')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    employee_id = fields.Integer(string='Employee Id')
    address = fields.Char(string='Address')
    image = fields.Image(string='Images')
    date_of_birth = fields.Date(string='DOB')
    age = fields.Integer(string='Age')
    designation = fields.Selection([('storemanager','Store Manager'),
                                   ('assistantmanager','Assistant Manager'),
                                   ('cashier','Cashier'),('stockclerk','Stock Clerk'),
                                    ('departmentmanager','Department Manager ')],
                                    'Designation')

