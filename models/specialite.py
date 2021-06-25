from odoo import models, fields, api


class Specialite(models.Model):
	_name = 'tp.hopital.specialite'
	_description = 'Table specialite'

	name = fields.Char(string="Specialité", required=True)
	code = fields.Char(string="Code", required=True)
	effectif = fields.Char(string="Nombre de medecin", compute='_compute_effectif')
	medecins_ids = fields.One2many(
        'tp.hopital.medecin', 'specialite_id', 'Liste des medecins')


	def _compute_effectif(self):
		self.effectif = len(self.medecins_ids)



