from odoo import models, fields

class Expense(models.Model):
    _name = 'expense'
    _description = 'Gasto'

    reservation_id = fields.Many2one('reservation', string='Reserva')
    type = fields.Char(string='Tipo de gasto')
    amount = fields.Float(string='Monto')