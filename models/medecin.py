from odoo import models, fields


class Medecins(models.Model):
    _name = 'tp.hopital.medecin'
    _description = 'Table medecin'

    name = fields.Char(string="Nom et Prenoms", required=True)
    matricule = fields.Char(string="Matricule")
    salaire = fields.Integer(string="Salaire")
    grade_id = fields.Many2one('tp.hopital.grade', string="Liste des grades")
    specialite_id = fields.Many2one('tp.hopital.specialite', string="Liste des specialite")
