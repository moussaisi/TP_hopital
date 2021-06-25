from odoo import models, fields, api


class Grades(models.Model):
	_name = 'tp.hopital.grade'
	_description = 'Table grade'

	name = fields.Char(string="Grade", required=True)
	code = fields.Char(string="Code", required=True)
	effectif = fields.Char(string="Nombre de medecin", compute='_compute_effectif')
	medecins_ids = fields.One2many(
        'tp.hopital.medecin', 'grade_id', 'Liste des medecins')


	def _compute_effectif(self):
		self.effectif = len(self.medecins_ids)
