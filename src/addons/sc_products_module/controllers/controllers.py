# -*- coding: utf-8 -*-
from odoo import http

 class sc_product_controller(http.Controller):
     @http.route('/sc_products_module/', auth='user')
     def index(self, **kw):
         return "SiedCloud - Products"

     @http.route('/sc_products_module/products/', auth='user')
     def list(self, **kw):
         return http.request.render('my_module.listing', {
             'root': '/sc_products_module/my_module',
             'objects': http.request.env['sc_products_module.my_module'].search([]),
         })

     @http.route('/sc_products_module/objects/<model("my_module.my_module"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('my_module.object', {
             'object': obj
         })