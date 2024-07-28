from odoo import models, fields

class OperatingRoom(models.Model):
    _name = 'operating.room'
    _description = 'Sala de operaciones'

    name = fields.Char(string='Nombre')
    capacity = fields.Integer(string='Capacidad')