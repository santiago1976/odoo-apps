# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime

class departamento_config(models.Model):
	_name = 'departamento_config'
	name = fields.Char('Departamento', required=True)