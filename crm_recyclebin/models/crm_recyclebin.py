# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo import exceptions

import logging
_logger = logging.getLogger(__name__) 

class crm_recyclebin(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def unlink(self):
        estado_lead = self.active
        if estado_lead:
            self.active = False
            return False
        else:
            return models.Model.unlink(self)
        
    @api.one 
    def recuperar_lead(self):
        self.active = True
        return True