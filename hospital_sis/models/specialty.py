# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Specialty(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'sis.specialty'
    # field to use for labeling records
    _rec_name = 'name'
    # the model's informal name
    _description = 'Hospital Specialties'
    # default order field for searching results
    _order = 'name'

    name = fields.Char(string="Name", size=80, required=True, help='Enter the Specialty Name')
