# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime

class asset_extends(models.Model):
	_inherit = 'account.asset.asset'
	serialnum = fields.Char('Num de Serie')
	asignadoa = fields.Many2one("res.users","Asignado a")
