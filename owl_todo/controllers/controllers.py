# -*- coding: utf-8 -*-
# from odoo import http


# class OwlTodo(http.Controller):
#     @http.route('/owl_todo/owl_todo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_todo/owl_todo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_todo.listing', {
#             'root': '/owl_todo/owl_todo',
#             'objects': http.request.env['owl_todo.owl_todo'].search([]),
#         })

#     @http.route('/owl_todo/owl_todo/objects/<model("owl_todo.owl_todo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_todo.object', {
#             'object': obj
#         })
