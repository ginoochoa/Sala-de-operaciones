from odoo import models, fields

class Hospitalization(models.Model):
    _name = 'hospitalization'
    _description = 'Hospitalización'

    reservation_id = fields.Many2one('reservation', string='Reserva')
    start_date = fields.Date(string='Fecha de inicio')
    end_date = fields.Date(string='Fecha de fin')
    room_type = fields.Char(string='Tipo de habitación')