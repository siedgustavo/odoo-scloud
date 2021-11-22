# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class sc_product(models.Model):
     _name = 'sc_product.product'

     name = fields.Char()
     description = fields.Text()
     product_category_id = fields.many2one('sc_product_category.category')
     price = fields.Integer()


class sc_product_category(models.Model):
    _name = 'sc_product_category.category'

    name = fields.Char()
    product_type_id = fields.many2one('sc_product_type.type')
    description = fields.Text()

class sc_product_type(models.Model):
    _name = 'sc_product_type.type'

    name = fields.Char()
    description = fields.Text()