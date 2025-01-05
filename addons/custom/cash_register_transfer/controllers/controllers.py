# -*- coding: utf-8 -*-
# from odoo import http


# class CashRegisterTransfer(http.Controller):
#     @http.route('/cash_register_transfer/cash_register_transfer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cash_register_transfer/cash_register_transfer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cash_register_transfer.listing', {
#             'root': '/cash_register_transfer/cash_register_transfer',
#             'objects': http.request.env['cash_register_transfer.cash_register_transfer'].search([]),
#         })

#     @http.route('/cash_register_transfer/cash_register_transfer/objects/<model("cash_register_transfer.cash_register_transfer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cash_register_transfer.object', {
#             'object': obj
#         })

