# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    dbm_v = fields.Integer(string="Condicion demasiado verde",default=5)
    dbm_r = fields.Integer(string="Condicion demasiado rojo",default=1)
    be_mta_mon = fields.Boolean(string='Es monitoreado por MTA', default=True)
    lt = fields.Integer(string='Tiempo de respuesta del proveedor')
    loteOptimo = fields.Integer(string='Lote óptimo')
    qty_transit = fields.Integer(string='# transito')
    
    @api.model
    def create(self,values):
        override_create = super(ProductProduct,self).create(values)
        product_info={'product_tmpl_id':override_create.id,'be_mta_mon':override_create.be_mta_mon,'dbm_v':override_create.dbm_v,'dbm_r':override_create.dbm_r,'lt':override_create.lt,'loteOptimo':override_create.loteOptimo,'qty_trasit':override_create.qty_transit}
        self.env['mta.producto'].create(product_info)
        return override_create