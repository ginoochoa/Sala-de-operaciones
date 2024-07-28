from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'reservation'
    _description = 'Reserva de sala de operaciones'

    all_day = fields.Boolean(string='All Day')
    date = fields.Date(string='Fecha de la reserva')
    operating_room_id = fields.Many2one('operating.room', string='Sala de operaciones')
    start_time = fields.Datetime(string='Hora de inicio')
    end_time = fields.Datetime(string='Hora de fin')
    patient_name = fields.Char(string='Nombre del paciente')
    procedure = fields.Char(string='Procedimiento')
    rooms = fields.Many2many('operating.room', string='Salas de operaciones')
    rooms_text = fields.Char(compute='_compute_rooms_text', string='Salas de operaciones')
    
    @api.depends('rooms')
    def _compute_rooms_text(self):
        for record in self:
            rooms_text = ', '.join(record.rooms.mapped('name'))
            record.rooms_text = rooms_text