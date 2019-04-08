# -*- coding: utf-8 -*-
{
	'name': "sat_demo",
	'summary': """A demo to manage your Customer Service. """,
	'description': """A demo to manage your Customer Service.""",
	'author': "Santiago Carbonell Forment",
	'website': "https://es.linkedin.com/in/carbonellsantiago",
	'category': 'Sales',
	'version': '0.1',
	'license': 'AGPL-3',
	'depends': ['base','sale'],
	'data': [
				'security/ir.model.access.csv',
				'views/satdemo_view.xml'],
	'images': ['static/description/banner.png'],
	'demo': [],
}