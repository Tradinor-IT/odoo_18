# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentRecord(models.Model):
     _name = 'strudent.record'
     _description = 'Student Record'

     admission_date                 = fields.Char(string="Admission Date",                      help="To mention the admission date")
     first_name                     = fields.Char(string="First Name",          required=True,  help="Student first name")
     last_name                      = fields.Char(string="Last Name",           required=True,  help="Student last name")
     father                         = fields.Char(string="Father",              required=True,  help="Father name")
     mother                         = fields.Char(string="Mother",              required=True,  help="Mother name")
     communication_address          = fields.Char(string="Communication Address",               help="Student Address")
     permanent_address              = fields.Char(string="Permanent Address",                   help="Student Permanent Address")
     same_as_communication_address  = fields.Char(string="Same as communication Address",       help="Enable if the Student Communication Address and Permanent Address is same")
     phone                          = fields.Char(string="Phone",                               help="Guardian contact number")
     email                          = fields.Char(string="Email",                               help="Guardian mail")
     mark                           = fields.Float(string="Previous Mark",)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
