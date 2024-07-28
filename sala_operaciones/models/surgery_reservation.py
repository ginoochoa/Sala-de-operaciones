from odoo import models, fields
class SurgeryReservation(models.Model):
    _name = 'surgery.reservation'
    _description = 'Reserva de sala de operaciones'

    date = fields.Date(string='Fecha')
    patient = fields.Many2one('res.partner', string='Paciente', required=True)
    operating_room_id = fields.Many2one('operating.room', string='Sala de operaciones')
    start_time = fields.Datetime(string='Hora de inicio')
    end_time = fields.Datetime(string='Hora de fin')
    



class OperatingRoom(models.Model):
    _name = 'operating.room'
    _description = 'Sala de operaciones'

    name = fields.Char(string='Nombre de la sala')
    capacity = fields.Integer(string='Capacidad de la sala')