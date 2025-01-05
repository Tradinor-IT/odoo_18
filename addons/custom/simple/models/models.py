# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'simple.book'
    _description = 'Book'

    name            = fields.Char(  string='Title', required=True)
    author          = fields.Char(  string='Author')
    published_date  = fields.Date(  string="Published Date")
    price           = fields.Float( string='Price')
