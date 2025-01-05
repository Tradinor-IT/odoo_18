from odoo import models, fields

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    allowed_user_ids = fields.Many2many(
            'res.users',
            string = 'Allowed Users',
            help = 'Users allowed to access this price list'
            )
