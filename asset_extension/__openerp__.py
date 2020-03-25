# -*- coding: utf-8 -*-
{
	'name': "Asset Extension",
	'summary': """An app that extends Asset functionality in Odoo """,
	'description': """Extends Assets in Odoo, adding an asign and a serialnumber fields""",
	'author': "Santiago Carbonell Forment",
	'website': "https://es.linkedin.com/in/carbonellsantiago",
	'category': 'Financials',
	'version': '0.1',
	'license': 'AGPL-3',
	'depends': ['base','account_accountant'],
	'data': [
		'views/asset_extend.xml',
	],
	'images': ['static/description/banner.png'],
	'demo': [],
}