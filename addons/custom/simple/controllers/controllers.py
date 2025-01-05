# -*- coding: utf-8 -*-
# from odoo import http


# class Simple(http.Controller):
#     @http.route('/simple/simple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple/simple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple.listing', {
#             'root': '/simple/simple',
#             'objects': http.request.env['simple.simple'].search([]),
#         })

#     @http.route('/simple/simple/objects/<model("simple.simple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple.object', {
#             'object': obj
#         })

