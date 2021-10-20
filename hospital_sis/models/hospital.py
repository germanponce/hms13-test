# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Hospital(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.hospital'
    # field to use for labeling records
    _rec_name = 'name'
    # the model's informal name
    _description = 'Hospitals'
    # default order field for searching results
    _order = 'name'

    name = fields.Char(string="Hospital Name", size=80, required=True,
                       help='Enter the Hospital Name')
    country_id = fields.Many2one(comodel_name='res.country', string="Country",
                                 required=False, ondelete='restrict')
