# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    @api.model
    def create(self,values):
        # your logic goes here
        print("entra aquí")
        #print(values)
        #product_info={'product_tmpl_id':values['id']}
        #self.env['mta.producto'].create(product_info)
        override_create = super(ProductProduct,self).create(values)
        print(override_create)
        print(type(override_create))
        return override_create