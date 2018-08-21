# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime

class departamento_contacto(models.Model):
	_inherit = 'res.partner'
	departamento_id = fields.Many2one(
		"departamento_config",
		"Departamento")