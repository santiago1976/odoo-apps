# -*- coding: utf-8 -*-
{
	'name': "CRM Extension",
	'summary': """An app that extends CRM functionality in Odoo """,
	'description': """Extends CRM module in Odoo, adding contacts and activities views and departments contacts""",
	'author': "Santiago Carbonell Forment",
	'website': "https://es.linkedin.com/in/carbonellsantiago",
	'category': 'Sales',
	'version': '0.1',
	'license': 'AGPL-3',
	'depends': ['base','crm'],
	'data': [
		'security/ir.model.access.csv',
		'views/departamento_config.xml',
		'views/departamento_contacto.xml',
		'views/contactos.xml',
		'views/actividades.xml',
	],
	'images': ['static/description/banner.png'],
	'demo': [],
}