# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cash_register_transfer(models.Model):
#     _name = 'cash_register_transfer.cash_register_transfer'
#     _description = 'cash_register_transfer.cash_register_transfer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

