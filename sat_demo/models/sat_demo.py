# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime
from odoo import exceptions
import logging

class sat(models.Model):
	_name = 'sat.demo'
	descripcion = fields.Char('Descripción', required=True)
	fecha_creacion = fields.Date(string='Fecha Creación', default=datetime.today())
	fecha_cierre = fields.Date(string='Fecha Cierre')
	cliente = fields.Many2one('res.partner', 'Cliente', required=True)
	coste_estimado = fields.Integer()
	garantia = fields.Char('Garantia')
	tecnico = fields.Many2one('res.users', 'Técnico')
	factura = fields.Many2one('sale.order','Factura')
	estado = fields.Selection([
			('noiniciado', 'No iniciado'),
			('enprogreso', 'En Progreso'),
			('cancelado', 'Cancelado'),
			('finalizado', 'Finalizado'),
			],default='noiniciado')
	estado_progreso = fields.Selection([
			('endiagnostico', 'En Diagnóstico'),
			('esperacliente', 'En Espera Cliente'),
			('esperandopieza', 'En Espera Pieza'),
			('enfacturacion', 'En Facturación'),
			])
	sintomas = fields.Text('Síntomas')
	diagnostico = fields.Text('Diagnóstico')
	
	@api.multi
	def noiniciado_button(self):
		self.ensure_one()
		self.write({
			'estado':'noiniciado'
		})
		
	@api.multi
	def enprogreso_button(self):
		self.ensure_one()
		log = logging.getLogger("Valor de tecnico: ")
		log.info(self.tecnico.name)
		if (str(self.tecnico.name) == 'False') or (self.sintomas.encode('utf-8')=='<p><br></p>'):
			raise exceptions.Warning('You must fill in the symptoms and assign a technician before moving to In Progress')
			return True
		else:
			self.write({'estado':'enprogreso'})
		return True
		
	@api.multi
	def finalizado_button(self):
		self.ensure_one()		
		if (str(self.factura.name) == 'False') or (self.diagnostico.encode('utf-8')=='<p><br></p>'):
			raise exceptions.Warning('You must fill in the diagnosis and assign a budget / invoice before closing an incident')
			return True
		else:
			self.write({'estado':'finalizado'})
		return True
		
	@api.multi
	def cancelado_button(self):
		self.ensure_one()
		self.write({
			'estado':'cancelado',
		})