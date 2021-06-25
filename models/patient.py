from odoo import models, fields, api
from datetime import datetime
import string

class Patients(models.Model):
    _name = 'tp.hopital.patient'
    _description = 'Table Patient'

    name = fields.Char(string="Nom et Prenoms", compute='_compute_name')
    first_name = fields.Char(string="Prenom de famille", required=True)
    last_name = fields.Char(string="Nom de famille", required=True)
    date_naissance = fields.Date(required=False)
    sexe = fields.Selection(
        [('f', 'Femme'), ('m', 'Masculin')], required=False)
    email = fields.Char(string="Email Personel", required=False)
    tel = fields.Char(string="Telephone", required=False)
    prise_en_charge = fields.Char(
        string="Avez-vous une prise en charge ?", default=False)
    pourcentage = fields.Integer(string="Taux de couverture")
    prix_ticket = fields.Integer(string="Prix Ticket")
    num_dossier = fields.Char(string="Numero Dossier")
    image = fields.Binary(string="Photo Patient")
    date_inscription = fields.Datetime(
        string="Date d'inscription", default=fields.Datetime.now(), store=True)
    medecin_id = fields.Many2one('tp.hopital.medecin', string="Medecin")



    @api.depends('first_name','last_name')
    def _compute_name(self):
        self.name = (self.first_name or '')+' '+(self.last_name or '')


    
