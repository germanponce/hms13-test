# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'res.partner'
    # python-inherited models
    _inherit = 'res.partner'

    rut = fields.Char(string="RUT", required=False, size=10, help='Enter the RUT')
    age = fields.Integer(string="Age", required=False, size=3, help='Enter the Age')
    profession = fields.Char(string="Profession", required=False, size=10, help='Enter the Profession')
