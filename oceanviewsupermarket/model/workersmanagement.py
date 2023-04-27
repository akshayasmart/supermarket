from datetime import date

from odoo import _, models,fields, api
from odoo.exceptions import UserError


class WorkersManagement(models.Model):
    _name = 'worker.worker'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Employee Name',tracking=True)
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    employee_code = fields.Char(string='Employee Code')
    address = fields.Char(string='Address')
    image = fields.Image(string='Images')
    date_of_birth = fields.Date(string='DOB')
    age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    designation = fields.Selection([
        ('storemanager','Store Manager'),
        ('assistantmanager','Assistant Manager'),
        ('cashier','Cashier'),
        ('stockclerk','Stock Clerk'),
        ('departmentmanager','Department Manager ')], 'Designation'
    )
    status_bar = fields.Selection([
        ('temporary','Temporary'),
        ('permanent','Permanent'),],'Status Bar',default='temporary'
    )

    worker_status = fields.Selection([
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent'), ],
        'Worker Status')



    _sql_constraints = [
        ('employee_code_uniq', 'unique (employee_code)', 'The Employee Code must be unique !')
    ]

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, '%s (%s)' % (record.date_of_birth, record.name)))
        return res

    @api.onchange('first_name', 'last_name')
    def onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = '{} {}'.format(self.first_name, self.last_name)

    @api.onchange('date_of_birth')
    def _onchange_dob(self):
        if self.date_of_birth:
            current_date = date.today()
            current_year = current_date.year
            date_of_birth_year = self.date_of_birth.year
            self.age = current_year - date_of_birth_year

    @api.constrains('employee_code')
    def _constraints_employee_code(self):
        for record in self:
            if self.age < 18:
                raise UserError(_("Employee Age must be above 18!"))

    def set_worker_status(self, vals):
        if vals.get('worker_status') == 'temporary':
            vals['status_bar'] = 'temporary'
        elif vals.get('worker_status') == 'permanent':
            vals['status_bar'] = 'permanent'
        return vals

    def write(self, vals):
        vals = self.set_worker_status(vals)
        res = super(WorkersManagement, self).write(vals)
        return res



