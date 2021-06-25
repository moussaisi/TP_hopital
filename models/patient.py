from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
import string

class Patients(models.Model):
    _name = 'tp.hopital.patient'
    _description = 'Table Patient'

    name = fields.Char(string="Nom et Prenoms", compute='_compute_name')
    first_name = fields.Char(string="Prenom de famille", required=True)
    last_name = fields.Char(string="Nom de famille", required=True)
    date_naissance = fields.Date(required=False)
    sexe = fields.Selection([('f', 'Femme'), ('m', 'Masculin')], required=False)
    email = fields.Char(string="Email Personel", required=False)
    tel = fields.Char(string="Telephone", required=False)
    prise_en_charge = fields.Selection([('non', 'NON'), ('oui', 'OUI')], 
        string="Avez-vous une prise en charge ?", default='non')
    pourcentage = fields.Integer(string="Taux de couverture")
    prix_ticket = fields.Integer(string="Prix Ticket", compute='_compute_prix_ticket')
    num_dossier = fields.Char(string='Numéro de dossier', required=True, copy=False,
     readonly=True,index=True, default=lambda self: _('New'))
    image = fields.Binary(string="Photo Patient")
    date_inscription = fields.Datetime(
        string="Date d'inscription", default=fields.Datetime.now(), store=True)
    medecin_id = fields.Many2one('tp.hopital.medecin', string="Medecin")



    @api.depends('first_name','last_name')
    def _compute_name(self):
        self.name = (self.first_name or '')+' '+(self.last_name or '')

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('tp.hopital.patient') or '/'
        vals['num_dossier'] = seq
        return super(Patients, self).create(vals)

    @api.multi
    @api.depends('prise_en_charge')                          
    def _compute_prix_ticket(self):
        for record in self:
            if record.prise_en_charge == "non":
                record.prix_ticket = 2000
            else :
                record.prix_ticket = (2000*(100-record.pourcentage))/100


    
