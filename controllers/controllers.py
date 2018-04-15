# -*- coding: utf-8 -*-
from odoo import http

# class DocAlquileres(http.Controller):
#     @http.route('/doc_alquileres/doc_alquileres/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doc_alquileres/doc_alquileres/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doc_alquileres.listing', {
#             'root': '/doc_alquileres/doc_alquileres',
#             'objects': http.request.env['doc_alquileres.doc_alquileres'].search([]),
#         })

#     @http.route('/doc_alquileres/doc_alquileres/objects/<model("doc_alquileres.doc_alquileres"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doc_alquileres.object', {
#             'object': obj
#         })